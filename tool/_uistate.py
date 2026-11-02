import re
import sys

data = open(sys.argv[1], encoding="utf-8", errors="replace").read()
for attr in ("checked", "selected"):
    for m in re.finditer(r'content-desc="([^"]*)"[^>]*?' + attr + r'="true"', data):
        print(f"{attr.upper()}: {m.group(1)}")
print("checked=true count:", data.count('checked="true"'))
print("selected=true count:", data.count('selected="true"'))
