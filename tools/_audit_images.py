#!/usr/bin/env python3
"""Scan all Hören Teil 2 images for technical failures / blank renders.

Flags images that are likely bad:
  - corrupt/truncated (PIL can't load)
  - tiny byte size
  - near-blank: very low pixel variance, or one color dominates the frame
  - near-duplicate of another option in the same test (same render returned)
Prints a sorted list of suspects so we can eyeball + regenerate them.
"""
import os, sys, glob, hashlib
from collections import defaultdict
from PIL import Image, ImageStat

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")

def dominant_frac(im):
    im = im.convert("RGB").resize((64, 64))
    colors = im.getcolors(64 * 64) or []
    if not colors:
        return 1.0
    top = max(c for c, _ in colors)
    return top / float(64 * 64)

rows = []
hashes = defaultdict(list)  # test -> [(letter, phash-ish)]
for path in sorted(glob.glob(os.path.join(IMG, "ai-*", "t2", "*.png"))):
    rel = os.path.relpath(path, IMG)
    test = rel.split(os.sep)[0]
    letter = os.path.splitext(os.path.basename(path))[0]
    size = os.path.getsize(path)
    info = {"test": test, "letter": letter, "kb": size // 1024, "flags": []}
    try:
        im = Image.open(path); im.load()
    except Exception as e:
        info["flags"].append(f"CORRUPT:{e}")
        rows.append(info); continue
    g = im.convert("L")
    st = ImageStat.Stat(g)
    stdev = st.stddev[0]
    dom = dominant_frac(im)
    info["std"] = round(stdev, 1)
    info["dom"] = round(dom, 2)
    # crude perceptual hash: 8x8 grayscale, above/below mean
    small = g.resize((8, 8))
    px = list(small.getdata()); avg = sum(px) / len(px)
    bits = "".join("1" if p > avg else "0" for p in px)
    hashes[test].append((letter, bits))
    if size < 6000:
        info["flags"].append("TINY")
    if stdev < 18:
        info["flags"].append("LOW-VARIANCE")
    if dom > 0.72:
        info["flags"].append("ONE-COLOR-DOMINATES")
    rows.append(info)

# near-duplicate detection within a test (hamming distance on 64-bit hash)
def ham(a, b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))
dups = []
for test, lst in hashes.items():
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            d = ham(lst[i][1], lst[j][1])
            if d <= 6:
                dups.append((test, lst[i][0], lst[j][0], d))

suspects = [r for r in rows if r["flags"]]
print(f"scanned {len(rows)} images; {len(suspects)} flagged\n")
for r in sorted(suspects, key=lambda r: (r["test"], r["letter"])):
    extra = f" std={r.get('std')} dom={r.get('dom')} {r['kb']}KB"
    print(f"  {r['test']}/{r['letter']}  {','.join(r['flags'])}{extra}")
if dups:
    print(f"\nnear-duplicate pairs within a test ({len(dups)}):")
    for t, a, b, d in sorted(dups):
        print(f"  {t}: {a} ~ {b}  (hamming {d})")
print("\nsize distribution (KB): min %d / med %d / max %d" % (
    min(r['kb'] for r in rows),
    sorted(r['kb'] for r in rows)[len(rows)//2],
    max(r['kb'] for r in rows)))
