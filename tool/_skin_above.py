import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
im = np.array(Image.open(path).convert("RGB")).astype(int)

# count skin-colored pixels in bands ABOVE the hair top (y 330..400)
for y1, y2 in ((330, 360), (360, 380), (380, 400), (400, 430)):
    band = im[y1:y2, 380:700]
    r, g, b = band[:, :, 0], band[:, :, 1], band[:, :, 2]
    skin = (abs(r - 208) < 30) & (abs(g - 139) < 30) & (abs(b - 91) < 30)
    hair = (r < 60) & (g < 45) & (b < 45)
    print(f"y{y1}-{y2}: skin={int(skin.sum())}  hair={int(hair.sum())}")

# also: any skin pixel strictly above the topmost hair pixel?
dark = (im[:, :, 0] < 60) & (im[:, :, 1] < 45) & (im[:, :, 2] < 45)
ys, xs = np.nonzero(dark[300:800, 380:700])
top_y = ys.min() + 300
print("topmost hair y:", top_y)
above = im[300:top_y, 380:700]
r, g, b = above[:, :, 0], above[:, :, 1], above[:, :, 2]
skin = (abs(r - 208) < 30) & (abs(g - 139) < 30) & (abs(b - 91) < 30)
print("skin px above hair top:", int(skin.sum()))
