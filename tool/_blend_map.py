import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

region = im[370:530, 420:660]
r, g, b = region[:, :, 0], region[:, :, 1], region[:, :, 2]
# hair-over-skin blend ~ (84,56,37)
blend = (abs(r - 84) < 18) & (abs(g - 56) < 15) & (abs(b - 37) < 15)
print("blend px:", int(blend.sum()))
ys, xs = np.nonzero(blend)
if len(ys):
    print("bbox y:", ys.min() + 370, ys.max() + 370, " x:", xs.min() + 420, xs.max() + 420)

# coarse density map: 12 cols x 8 rows over region
H, W = blend.shape
rows, cols = 8, 12
for i in range(rows):
    line = ""
    for j in range(cols):
        blk = blend[i * H // rows:(i + 1) * H // rows, j * W // cols:(j + 1) * W // cols]
        d = blk.sum()
        line += "." if d == 0 else ("#" if d > 60 else ("+" if d > 20 else "-"))
    print(f"y={370 + i * H // rows:4d} {line}")
