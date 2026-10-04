#!/usr/bin/env python3
"""Generate Google Cloud TTS German samples for A/B vs edge-tts.

    export GOOGLE_TTS_API_KEY='...'
    python3 tools/sample_chirp.py              # Chirp 3 HD (default)
    python3 tools/sample_chirp.py --family neural2
    python3 tools/sample_chirp.py --family studio

Writes MP3s into audio_samples/. Open audio_samples/listen.html to compare.
LINEAR16 from the API is re-encoded at 48 kbps so bitrate matches edge-tts.
"""
import argparse, base64, json, os, subprocess, sys, tempfile, time, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "audio_samples"
API = "https://texttospeech.googleapis.com/v1/text:synthesize"

ANNOUNCE = (
    "Achtung: Der Regional-Express nach Hamburg fährt heute von Gleis fünf "
    "statt von Gleis drei. Bitte beachten Sie die geänderte Abfahrt."
)
DIALOG = (
    "Seit acht Jahren. Ich habe in einem kleinen Hotel gelernt und arbeite "
    "jetzt in einem Restaurant in Berlin. Die Arbeit ist anstrengend, aber ich liebe sie."
)

FAMILIES = {
    "chirp": [
        ("chirp-charon", "de-DE-Chirp3-HD-Charon", "m"),
        ("chirp-puck", "de-DE-Chirp3-HD-Puck", "m"),
        ("chirp-leda", "de-DE-Chirp3-HD-Leda", "f"),
        ("chirp-kore", "de-DE-Chirp3-HD-Kore", "f"),
    ],
    "neural2": [
        ("neural2-b", "de-DE-Neural2-B", "m"),
        ("neural2-d", "de-DE-Neural2-D", "m"),
        ("neural2-h", "de-DE-Neural2-H", "m"),
        ("neural2-c", "de-DE-Neural2-C", "f"),
        ("neural2-f", "de-DE-Neural2-F", "f"),
        ("neural2-g", "de-DE-Neural2-G", "f"),
    ],
    "studio": [
        ("studio-b", "de-DE-Studio-B", "m"),
        ("studio-c", "de-DE-Studio-C", "f"),
    ],
}


def synth(text, voice, key):
    body = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": "de-DE", "name": voice},
        "audioConfig": {
            "audioEncoding": "LINEAR16",
            "sampleRateHertz": 24000,
            "speakingRate": 1.0,
        },
    }).encode()
    req = urllib.request.Request(
        API,
        data=body,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "X-Goog-Api-Key": key,
        },
        method="POST",
    )
    last = None
    for attempt in range(1, 5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                payload = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", "replace")
            raise SystemExit(f"HTTP {e.code} for {voice}: {err}")
        except Exception as e:
            last = e
            print(f"  retry {attempt}/4: {e}", flush=True)
            time.sleep(2 * attempt)
    else:
        raise SystemExit(f"failed for {voice}: {last}")
    audio_b64 = payload.get("audioContent")
    if not audio_b64:
        raise SystemExit(f"no audioContent for {voice}: {payload}")
    return base64.b64decode(audio_b64)


def to_mp3(wav_bytes, dest):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(wav_bytes)
        wav_path = tmp.name
    try:
        subprocess.run([
            "ffmpeg", "-y", "-i", wav_path,
            "-codec:a", "libmp3lame", "-b:a", "48k", "-ar", "24000", "-ac", "1",
            str(dest),
        ], check=True, capture_output=True)
    finally:
        os.unlink(wav_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family", choices=sorted(FAMILIES), default="chirp")
    args = ap.parse_args()

    key = os.environ.get("GOOGLE_TTS_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        sys.exit("Set GOOGLE_TTS_API_KEY and rerun.")

    OUT.mkdir(parents=True, exist_ok=True)
    for slug, voice, _g in FAMILIES[args.family]:
        for kind, text in (("announce", ANNOUNCE), ("dialog", DIALOG)):
            dest = OUT / f"sample-{slug}-{kind}.mp3"
            print(f"{dest.name}  ←  {voice}", flush=True)
            to_mp3(synth(text, voice, key), dest)
            print(f"  {dest.stat().st_size // 1024} KB")
    print("\nDone. Open audio_samples/listen.html")


if __name__ == "__main__":
    main()
