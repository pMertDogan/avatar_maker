import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

# hair base color (44,27,24). Find pixels notably lighter but still hair-ish (not skin, not bg)
region = im[370:530, 420:660]
r, g, b = region[:, :, 0], region[:, :, 1], region[:, :, 2]
# lighter brown: r in 60..140, g 40..90, b 35..80 (between hair and skin)
lighter = (r > 55) & (r < 150) & (g > 35) & (g < 100) & (b > 30) & (b < 90)
print("lighter-hair px:", int(lighter.sum()))
ys, xs = np.nonzero(lighter)
if len(ys):
    print("bbox y:", ys.min() + 370, ys.max() + 370, " x:", xs.min() + 420, xs.max() + 420)
    # histogram of colors
    cols, cnts = np.unique(region[lighter].reshape(-1, 3), axis=0, return_counts=True)
    order = np.argsort(-cnts)[:6]
    for i in order:
        print("  ", tuple(cols[i]), int(cnts[i]))
