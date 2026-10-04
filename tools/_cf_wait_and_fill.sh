#!/usr/bin/env bash
# Probe-driven backfill: instead of guessing when Cloudflare's free Workers AI
# allocation resets (it's NOT a clean 00:00 UTC reset — looks like a rolling
# ~24h window), poll a cheap 1-image request every PROBE_EVERY seconds. The
# moment a probe returns HTTP 200 (cap lifted), run the CF generator in passes
# until all images exist. Generator skips existing files, so only the ~65
# missing get made.
set -u
cd "$(dirname "$0")/.."

RANGE="${1:-ai-75..ai-100}"
LO="${2:-75}"; HI="${3:-100}"
PROBE_EVERY="${PROBE_EVERY:-1800}"   # 30 min between probes while capped
MAX_PROBES="${MAX_PROBES:-96}"       # ~48h ceiling

export CF_ACCOUNT_ID="$(tr -d ' \t\r\n' < '/Users/user/basepaint generator/.cloudflare_account')"
export CF_API_TOKEN="$(tr -d ' \t\r\n' < '/Users/user/basepaint generator/.cloudflare_token')"
CF_URL="https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT_ID/ai/run/@cf/black-forest-labs/flux-1-schnell"

count_missing() {
  local m=0 n c
  for n in $(seq "$LO" "$HI"); do
    c=$(ls "assets/images/ai-$n/t2/"*.png 2>/dev/null | grep -c '\.png$')
    m=$((m + 9 - c))
  done
  echo "$m"
}

probe() {  # echo the HTTP code of a tiny generation request
  curl -s -o /dev/null -w "%{http_code}" --max-time 60 -X POST \
    -H "Authorization: Bearer $CF_API_TOKEN" -H "Content-Type: application/json" \
    -d '{"prompt":"a small grey dot on white","steps":4}' "$CF_URL"
}

fill() {  # run generator in passes until nothing is missing or we re-hit the cap
  for pass in 1 2 3 4 5 6 7 8; do
    [ "$(count_missing)" -eq 0 ] && { echo "ALL DONE — 900/900."; return 0; }
    echo "--- fill pass $pass  $(date -u '+%T')Z  missing $(count_missing) ---"
    python3 tools/generate_images_cf.py --test "$RANGE"
    [ "$(count_missing)" -eq 0 ] && { echo "ALL DONE — 900/900."; return 0; }
    # re-hit the cap mid-fill? wait for the next window
    echo "still missing $(count_missing); cap likely re-hit, sleep ${PROBE_EVERY}s"
    sleep "$PROBE_EVERY"
  done
  return 1
}

echo "$(date -u '+%F %T')Z  waiting for Cloudflare cap to lift; missing $(count_missing)"
for p in $(seq 1 "$MAX_PROBES"); do
  [ "$(count_missing)" -eq 0 ] && { echo "already complete"; exit 0; }
  code=$(probe)
  echo "$(date -u '+%T')Z  probe $p -> HTTP $code"
  if [ "$code" = "200" ]; then
    echo "cap lifted — starting fill"
    fill && exit 0
    echo "fill incomplete; resume probing"
  fi
  sleep "$PROBE_EVERY"
done
echo "Reached MAX_PROBES; $(count_missing) still missing."
exit 1
