import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

y1, y2, x1, x2 = 370, 480, 420, 660
region = im[y1:y2, x1:x2]
r, g, b = region[:, :, 0], region[:, :, 1], region[:, :, 2]
hair = (r < 60) & (g < 45) & (b < 45)
notbg = ~((abs(r - 238) < 8) & (abs(g - 238) < 8) & (abs(b - 238) < 8))
notskin = ~((abs(r - 208) < 25) & (abs(g - 139) < 25) & (abs(b - 91) < 25))
other = notbg & notskin & ~hair
print("hair:", int(hair.sum()), "other:", int(other.sum()))

H, W = hair.shape
rows, cols = 11, 24
for i in range(rows):
    line = ""
    for j in range(cols):
        ys, ye = i * H // rows, (i + 1) * H // rows
        xs, xe = j * W // cols, (j + 1) * W // cols
        hb = hair[ys:ye, xs:xe].sum()
        ob = other[ys:ye, xs:xe].sum()
        tot = (ye - ys) * (xe - xs)
        if hb > tot * 0.6:
            line += "#"
        elif ob > 8:
            line += "o"
        elif hb > tot * 0.15:
            line += "+"
        elif hb > 0 or ob > 0:
            line += "-"
        else:
            line += "."
    print(f"y={y1 + i * H // rows:4d} {line}")
