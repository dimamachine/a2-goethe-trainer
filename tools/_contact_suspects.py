#!/usr/bin/env python3
"""Build a labeled contact sheet of the lowest-variance (most likely blank/
failed) Teil-2 images so we can eyeball them. Sorted by stddev ascending."""
import os, glob
from PIL import Image, ImageStat, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "images")

cands = []
for path in glob.glob(os.path.join(IMG, "ai-*", "t2", "*.png")):
    try:
        im = Image.open(path); im.load()
    except Exception:
        cands.append((-1.0, path)); continue
    st = ImageStat.Stat(im.convert("L"))
    cands.append((st.stddev[0], path))
cands.sort(key=lambda x: x[0])
cands = cands[:48]  # 48 lowest-variance

cols, cell, pad, lab = 8, 150, 6, 16
rows = (len(cands) + cols - 1) // cols
W = cols * (cell + pad) + pad
H = rows * (cell + lab + pad) + pad
sheet = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 11)
except Exception:
    font = ImageFont.load_default()

for i, (std, path) in enumerate(cands):
    r, c = divmod(i, cols)
    x = pad + c * (cell + pad)
    y = pad + r * (cell + lab + pad)
    try:
        thumb = Image.open(path).convert("RGB").resize((cell, cell))
        sheet.paste(thumb, (x, y))
    except Exception:
        draw.rectangle([x, y, x + cell, y + cell], fill="#fdd")
    rel = os.path.relpath(path, IMG)
    tag = rel.split(os.sep)[0].replace("ai-", "") + "/" + os.path.splitext(os.path.basename(path))[0]
    draw.text((x, y + cell + 2), f"{tag} s{std:.0f}", fill="black", font=font)

out = os.path.join(ROOT, "tools", "_suspects_sheet.png")
sheet.save(out)
print("wrote", out, sheet.size)
print("lowest 12:", [(round(s,1), os.path.relpath(p, IMG).replace('/t2','').replace('/', ' ')) for s,p in cands[:12]])
