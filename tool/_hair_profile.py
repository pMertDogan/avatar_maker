import sys
import numpy as np
from PIL import Image

# usage: _hair_profile.py image.png
path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

# hair is very dark brown ~ (45,30,25)-(60,40,35); skin ~ (208,139,91)
h, w, _ = im.shape
dark = (im[:, :, 0] < 90) & (im[:, :, 1] < 70) & (im[:, :, 2] < 70)

# scan the avatar area only (upper half)
region_y1, region_y2 = 300, 800
for y in range(region_y1, region_y2, 10):
    xs = np.nonzero(dark[y, 300:780])[0]
    if len(xs) == 0:
        continue
    x1, x2 = xs.min() + 300, xs.max() + 300
    print(f"y={y}  hair x={x1}..{x2}  width={x2 - x1 + 1}")
