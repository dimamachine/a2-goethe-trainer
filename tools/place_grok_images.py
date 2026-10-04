#!/usr/bin/env python3
"""Helper to convert Grok-generated JPGs (from image_gen tool) into the
correct assets/images/<tid>/t2/<letter>.png at 512x512 PNG.

Usage examples:
  # Place specific
  python3 tools/place_grok_images.py --map ai-3:a=35.jpg,ai-3:b=36.jpg ...

  # Or edit the BATCH list inside for a wave and run
  python3 tools/place_grok_images.py --batch-wave

The script always resizes to 512x512 and saves optimized PNG.
"""
import argparse
import json
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_DEFAULT = os.path.expanduser(
    "~/.grok/sessions/%2FUsers%2Fuser%2FA2-Goethe-AI/019ee160-bf19-7973-9dc0-6f6c9100b2e1/images/"
)

def place(tid, letter, src_jpg_path, session_dir=None):
    if session_dir is None:
        session_dir = SESSION_DEFAULT
    if not os.path.isabs(src_jpg_path):
        src = os.path.join(session_dir, src_jpg_path)
    else:
        src = src_jpg_path
    if not os.path.exists(src):
        raise FileNotFoundError(src)

    out_dir = os.path.join(ROOT, "assets", "images", tid, "t2")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, f"{letter}.png")

    im = Image.open(src).convert("RGBA")
    im = im.resize((512, 512), Image.LANCZOS)
    if im.mode == "RGBA":
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg.convert("RGB")
    else:
        im = im.convert("RGB")
    im.save(dst, "PNG", optimize=True)
    print(f"{tid} {letter} -> {dst} ({os.path.getsize(dst)//1024} KB)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--map", help="Comma list tid:letter=jpgname e.g. ai-5:a=40.jpg,ai-5:b=41.jpg")
    ap.add_argument("--drop", help="Folder containing generated jpgs named like ai-7-a.jpg or a.jpg (for current tid)")
    ap.add_argument("--for-test", help="When using --drop, specify the test id e.g. ai-7")
    ap.add_argument("--session", default=SESSION_DEFAULT)
    args = ap.parse_args()

    if args.map:
        for item in args.map.split(","):
            item = item.strip()
            if not item: continue
            left, jpg = item.split("=")
            tid, letter = left.split(":")
            place(tid.strip(), letter.strip(), jpg.strip(), args.session)
    elif args.drop:
        if not args.for_test:
            print("When using --drop you must also pass --for-test ai-7")
            return
        tid = args.for_test
        for letter in "abcdefghi":
            for candidate in [f"{tid}-{letter}.jpg", f"{letter}.jpg", f"{letter.upper()}.jpg"]:
                p = os.path.join(args.drop, candidate)
                if os.path.exists(p):
                    place(tid, letter, p, args.session)
                    break
        else:
            print(f"No image found for {tid} {letter}")
    else:
        print("Use --map or --drop --for-test ...")

if __name__ == "__main__":
    main()
