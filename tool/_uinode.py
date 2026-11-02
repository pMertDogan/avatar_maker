import re
import sys

data = open(sys.argv[1], encoding="utf-8", errors="replace").read()
nodes = re.findall(
    r'<node[^>]*?content-desc="([^"]*)"[^>]*?bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"',
    data,
)
pat = sys.argv[2] if len(sys.argv) > 2 else None
for desc, x1, y1, x2, y2 in nodes:
    if not desc:
        continue
    if pat and pat.lower() not in desc.lower():
        continue
    cx = (int(x1) + int(x2)) // 2
    cy = (int(y1) + int(y2)) // 2
    print(f"{desc}  center=({cx},{cy})  bounds=({x1},{y1})-({x2},{y2})")
