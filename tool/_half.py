import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

# whole hair cap above the fringe (y 375..475), full width
region = im[375:475, 420:660]
cols, cnts = np.unique(region.reshape(-1, 3), axis=0, return_counts=True)
order = np.argsort(-cnts)
print("unique colors in hair cap:", len(cols))
shown = 0
for i in order:
    c = tuple(int(v) for v in cols[i])
    n = int(cnts[i])
    if n < 5:
        continue
    print("  ", c, n)
    shown += 1
    if shown >= 12:
        break

# split left vs right half
for name, sl in (("LEFT x420-540", region[:, :120]), ("RIGHT x540-660", region[:, 120:])):
    cols, cnts = np.unique(sl.reshape(-1, 3), axis=0, return_counts=True)
    order = np.argsort(-cnts)
    top = [(tuple(int(v) for v in cols[i]), int(cnts[i])) for i in order[:4]]
    print(name, top)
