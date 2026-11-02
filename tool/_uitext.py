import re
import sys

data = open(sys.argv[1], encoding="utf-8", errors="replace").read()
texts = re.findall(r'text="([^"]*)"', data)
descs = re.findall(r'content-desc="([^"]*)"', data)
print("TEXTS:", [t for t in texts if t])
print("DESCS:", [d for d in descs if d])
