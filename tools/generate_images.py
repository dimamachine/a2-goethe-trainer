#!/usr/bin/env python3
"""Generate textbook-style picture options for Hören Teil 2.

Free, keyless image generation via Pollinations.ai (model "sana"). Images are
downloaded as static PNGs into assets/images/<test-id>/t2/<letter>.png so the
site stays fully offline once generated. Like assets/audio, this folder is
gitignored (AI-only content) and never committed.

Each Teil-2 option is an *action/object* (e.g. "packt die Koffer"); we don't
draw the German text, we draw a clear visual concept for it. A fixed style
prefix keeps the 9 images of one test looking like a consistent set.

Usage:
  python3 tools/generate_images.py --test ai-1        # one test, Teil 2
  python3 tools/generate_images.py --test ai-1 --force # re-download existing
"""
import argparse, json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Consistent "German A2 textbook" look.
# Style tuned to match official Goethe-Zertifikat A2 exam books
# (Modellsatz / Übungssatz candidate sheets) as seen in reference materials:
# colorful cartoon illustrations, clear black outlines, flat bright colors
# with subtle shading, friendly cartoon people/objects, single clear scene,
# plain white background, highly readable at small size, no text inside.
STYLE = (
    "simple colorful cartoon illustration in the style of official "
    "Goethe-Zertifikat A2 Hören exam books (Modellsatz, Übungssatz), "
    "clear black outlines, flat bright friendly colors with subtle shading, "
    "cartoon people or objects performing one clear everyday activity, "
    "plain white background, clean composition, highly readable even at "
    "small thumbnail size, minimal details, no text, no words, no letters, "
    "no captions, centered"
)

# Hand-authored visual concept per German option text, keyed by the normalized
# (lowercased, stripped) German text. Lives in tools/_image_concepts.json so it
# can grow toward all ~829 unique options. If a text has no entry we fall back
# to passing the German text straight to the model.
CONCEPTS_PATH = os.path.join(ROOT, "tools", "_image_concepts.json")


def load_concepts():
    if not os.path.exists(CONCEPTS_PATH):
        return {}
    return json.load(open(CONCEPTS_PATH, encoding="utf-8"))


def load_tests():
    """Read window.HOEREN_TESTS = [...] from the JS data file as JSON."""
    p = os.path.join(ROOT, "assets", "data", "hoeren-tests.js")
    txt = open(p, encoding="utf-8").read()
    start = txt.index("[", txt.index("window.HOEREN_TESTS"))
    # find matching close: the file ends the array with "\n];"
    end = txt.rindex("];")
    return json.loads(txt[start:end + 1])


# Pollinations free tier (as of 2026-06): "flux"/"turbo" are legacy/paid and
# return HTTP 402; the free model is "sana". Free tier allows only 1 request
# queued per IP, so we MUST go strictly sequential with a pause between calls.
MODEL = os.environ.get("POLLI_MODEL", "sana")
PACE = float(os.environ.get("POLLI_PACE", "4"))  # seconds between requests
ATTEMPTS = int(os.environ.get("POLLI_ATTEMPTS", "8"))  # tries per image
# Circuit breaker: if this many images in a row give up (e.g. IP is being
# 402-throttled hard), abort the whole pass so an outer retry loop can sleep
# and try again later instead of churning for hours writing nothing. 0=off.
ABORT_AFTER = int(os.environ.get("POLLI_ABORT_AFTER", "0"))
_consec_fail = 0


class RateLimited(Exception):
    pass


class AbortRun(Exception):
    pass


def fetch(prompt, dest, seed):
    q = urllib.parse.quote(prompt)
    url = (f"https://image.pollinations.ai/prompt/{q}"
           f"?width=512&height=512&nologo=true&model={MODEL}&seed={seed}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            ctype = r.headers.get("Content-Type", "")
            data = r.read()
    except urllib.error.HTTPError as e:
        if e.code == 402:
            raise RateLimited("402 queue full / rate limited")
        raise
    # error responses come back as small JSON bodies, not images
    if "image" not in ctype or len(data) < 2000 or data[:2] not in (b"\xff\xd8", b"\x89P"):
        if data[:1] == b"{":
            raise RateLimited("got JSON error body instead of image")
        raise RuntimeError(f"unexpected response ({len(data)} bytes, {ctype})")
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def gen_test(t, concepts, force):
    """Generate the 9 Teil-2 picture options for one test."""
    tid = t["id"]
    opts = t["teile"][1]["options"]
    out = os.path.join(ROOT, "assets", "images", tid, "t2")
    os.makedirs(out, exist_ok=True)
    print(f"{tid} Teil 2 — {len(opts)} options -> {out}")
    missing = 0
    for i, o in enumerate(opts):
        letter, text = o["letter"], o["text"]
        dest = os.path.join(out, f"{letter}.png")
        if os.path.exists(dest) and not force:
            print(f"  {letter}  skip (exists)")
            continue
        key = text.strip().lower()
        # test-scoped override ("ai-55|köln") wins over the shared key ("köln"),
        # so the same word can mean different things in different tests
        concept = concepts.get(f"{tid}|{key}") or concepts.get(key)
        if not concept:
            missing += 1
            concept = text  # fall back to raw German
        prompt = f"{concept}. {STYLE}"
        seed = 1000 + i  # deterministic per-slot seed so re-runs are stable
        ok = False
        for attempt in range(1, ATTEMPTS + 1):
            try:
                n = fetch(prompt, dest, seed)
                tag = "" if (concepts.get(f"{tid}|{key}") or concepts.get(key)) else "  [no concept]"
                print(f"  {letter}  ok ({n // 1024} KB)  «{text}»{tag}", flush=True)
                ok = True
                break
            except RateLimited as e:
                # free tier: only 1 queued request/IP — wait for the slot
                wait = min(8 + 6 * attempt, 40)
                print(f"  {letter}  rate-limited ({e}); wait {wait}s", flush=True)
                time.sleep(wait)
            except Exception as e:
                print(f"  {letter}  attempt {attempt} failed: {e}", flush=True)
                time.sleep(4 * attempt)
        global _consec_fail
        if ok:
            _consec_fail = 0
        else:
            print(f"  {letter}  GAVE UP", flush=True)
            _consec_fail += 1
            if ABORT_AFTER and _consec_fail >= ABORT_AFTER:
                raise AbortRun(f"{_consec_fail} consecutive give-ups — IP likely "
                               f"throttled; aborting pass for outer retry loop")
        time.sleep(PACE)  # pace requests so we don't trip the queue limit
    return missing


def expand_ids(spec, tests):
    """Accept 'ai-1', 'ai-1..ai-5', or comma lists."""
    ids = []
    for part in spec.split(","):
        part = part.strip()
        if ".." in part:
            a, b = part.split("..")
            lo, hi = int(a.split("-")[1]), int(b.split("-")[1])
            ids += [f"ai-{n}" for n in range(lo, hi + 1)]
        elif part:
            ids.append(part)
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", required=True,
                    help="test id(s): 'ai-1', 'ai-1..ai-5', or 'ai-1,ai-3'")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    tests = load_tests()
    by_id = {x.get("id"): x for x in tests}
    concepts = load_concepts()
    print(f"loaded {len(concepts)} hand-authored concepts")

    total_missing = 0
    try:
        for tid in expand_ids(args.test, tests):
            t = by_id.get(tid)
            if not t:
                print(f"!! {tid} not found, skipping")
                continue
            total_missing += gen_test(t, concepts, args.force)
    except AbortRun as e:
        print(f"\nABORT: {e}", flush=True)
        sys.exit(75)  # signal the outer retry loop to back off and try later
    if total_missing:
        print(f"\nNOTE: {total_missing} option(s) had no hand-authored concept "
              f"(used raw German). Add them to tools/_image_concepts.json.")


if __name__ == "__main__":
    main()
