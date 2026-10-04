#!/usr/bin/env python3
"""Generate Hören Teil 2 picture options via Cloudflare Workers AI.

Drop-in alternative to generate_images.py for when Pollinations' free tier is
blocking our IP. Uses the free Workers AI model @cf/black-forest-labs/flux-1-schnell.
Reuses the same hand-authored concepts, style prefix and output layout
(assets/images/<test-id>/t2/<letter>.png), so it backfills seamlessly and
skips already-generated files.

Credentials (free Cloudflare account) via env:
  CF_ACCOUNT_ID  — dashboard account id
  CF_API_TOKEN   — API token with "Workers AI" permission

Usage:
  CF_ACCOUNT_ID=... CF_API_TOKEN=... \
    python3 tools/generate_images_cf.py --test "ai-75..ai-100"
  ... --force   # re-download existing
"""
import argparse, base64, json, os, sys, time, urllib.request, urllib.error

# reuse the shared concept/test loaders, style prefix and id expansion
from generate_images import (STYLE, load_concepts, load_tests, expand_ids,
                             ROOT)

MODEL = os.environ.get("CF_MODEL", "@cf/black-forest-labs/flux-1-schnell")
STEPS = int(os.environ.get("CF_STEPS", "6"))      # 1..8, more = better/slower
PACE = float(os.environ.get("CF_PACE", "0.5"))    # gentle gap between requests
ACCOUNT = os.environ.get("CF_ACCOUNT_ID", "")
TOKEN = os.environ.get("CF_API_TOKEN", "")


def fetch_cf(prompt, dest):
    """POST the prompt to Workers AI, decode the base64 image, write to dest."""
    url = (f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}"
           f"/ai/run/{MODEL}")
    body = json.dumps({"prompt": prompt[:2048], "steps": STEPS}).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=120) as r:
        payload = json.loads(r.read())
    if not payload.get("success"):
        raise RuntimeError(f"API error: {payload.get('errors')}")
    b64 = payload["result"]["image"]
    data = base64.b64decode(b64)
    if len(data) < 2000 or data[:2] not in (b"\xff\xd8", b"\x89P"):
        raise RuntimeError(f"unexpected image data ({len(data)} bytes)")
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def gen_test(t, concepts, force):
    tid = t["id"]
    opts = t["teile"][1]["options"]
    out = os.path.join(ROOT, "assets", "images", tid, "t2")
    os.makedirs(out, exist_ok=True)
    print(f"{tid} Teil 2 — {len(opts)} options -> {out}", flush=True)
    missing = 0
    for o in opts:
        letter, text = o["letter"], o["text"]
        dest = os.path.join(out, f"{letter}.png")
        if os.path.exists(dest) and not force:
            print(f"  {letter}  skip (exists)")
            continue
        key = text.strip().lower()
        concept = concepts.get(f"{tid}|{key}") or concepts.get(key)
        if not concept:
            missing += 1
            concept = text
        prompt = f"{concept}. {STYLE}"
        ok = False
        for attempt in range(1, 6):
            try:
                n = fetch_cf(prompt, dest)
                print(f"  {letter}  ok ({n // 1024} KB)  «{text}»", flush=True)
                ok = True
                break
            except urllib.error.HTTPError as e:
                msg = e.read()[:200].decode("utf-8", "replace")
                print(f"  {letter}  HTTP {e.code} attempt {attempt}: {msg}",
                      flush=True)
                # 429 = rate limit / daily cap; back off a bit longer
                time.sleep(5 * attempt if e.code == 429 else 3 * attempt)
            except Exception as e:
                print(f"  {letter}  attempt {attempt} failed: {e}", flush=True)
                time.sleep(3 * attempt)
        if not ok:
            print(f"  {letter}  GAVE UP", flush=True)
        time.sleep(PACE)
    return missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", required=True,
                    help="test id(s): 'ai-1', 'ai-75..ai-100', or 'ai-1,ai-3'")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not ACCOUNT or not TOKEN:
        sys.exit("Set CF_ACCOUNT_ID and CF_API_TOKEN env vars first.")

    tests = load_tests()
    by_id = {x.get("id"): x for x in tests}
    concepts = load_concepts()
    print(f"loaded {len(concepts)} hand-authored concepts; model {MODEL}")

    total_missing = 0
    for tid in expand_ids(args.test, tests):
        t = by_id.get(tid)
        if not t:
            print(f"!! {tid} not found, skipping")
            continue
        total_missing += gen_test(t, concepts, args.force)
    if total_missing:
        print(f"\nNOTE: {total_missing} option(s) had no hand-authored concept "
              f"(used raw German).")


if __name__ == "__main__":
    main()
