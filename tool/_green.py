import sys
import numpy as np
from PIL import Image

im = np.array(Image.open(sys.argv[1]).convert("RGB")).astype(int)
# bright green selection box
mask = (im[:, :, 1] > 200) & (im[:, :, 0] < 120) & (im[:, :, 2] < 120)
ys, xs = np.nonzero(mask)
if len(ys) == 0:
    print("no green")
else:
    print("green box x:", xs.min(), xs.max(), "y:", ys.min(), ys.max())
    print("center:", (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2)
    # estimate pitch: find other green? none. print row of icons: detect dark pixels rows
