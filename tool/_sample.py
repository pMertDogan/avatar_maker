import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

# sample points: (x, y, label)
pts = [
    (500, 430, "hair-left"),
    (560, 430, "hair-right-patch"),
    (540, 400, "hair-top"),
    (470, 470, "hair-mid-left"),
    (600, 460, "hair-mid-right"),
    (540, 520, "forehead-just-below-hair"),
    (540, 370, "above-hair(bg)"),
]
for x, y, label in pts:
    print(f"{label} ({x},{y}): {tuple(im[y, x])}")

# find all pixels in hair region that are skin-ish (bare scalp)
region = im[380:520, 430:650]
skin = (abs(region[:, :, 0] - 208) < 30) & (abs(region[:, :, 1] - 139) < 30) & (abs(region[:, :, 2] - 91) < 30)
print("skin-colored px inside hair bbox:", int(skin.sum()))
ys, xs = np.nonzero(skin)
if len(ys):
    print("  bbox y:", ys.min() + 380, ys.max() + 380, " x:", xs.min() + 430, xs.max() + 430)
