import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

for y in range(385, 475, 15):
    row = []
    for x in range(470, 645, 25):
        row.append(f"{tuple(int(v) for v in im[y, x])}")
    print(f"y={y}: " + " ".join(row))
