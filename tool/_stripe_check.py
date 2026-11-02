import sys
import numpy as np
from PIL import Image

# usage: _stripe_check.py image.png x1 y1 x2 y2 [label]
path = sys.argv[1]
x1, y1, x2, y2 = (int(v) for v in sys.argv[2:6])
label = sys.argv[6] if len(sys.argv) > 6 else path

im = np.array(Image.open(path).convert("RGB"))
region = im[y1:y2, x1:x2]

# vertical scan through the middle: list color transitions
xc = region.shape[1] // 2
col = region[:, xc]
runs = []
prev = None
start = 0
for i, px in enumerate(col):
    t = tuple(px)
    if t != prev:
        if prev is not None:
            runs.append((prev, i - start))
        prev = t
        start = i
runs.append((prev, len(col) - start))

print(f"== {label} column transitions (x={x1 + xc}) ==")
for color, length in runs:
    if length >= 2:
        print(f"  {color} x{length}")

# unique colors in region
colors, counts = np.unique(region.reshape(-1, 3), axis=0, return_counts=True)
order = np.argsort(-counts)[:8]
print("top colors:")
for i in order:
    print(f"  {tuple(colors[i])} count={counts[i]}")
