import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
box = tuple(int(v) for v in sys.argv[3:7])
im = Image.open(src).crop(box)
im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
im.save(dst)
print(dst, im.size)
