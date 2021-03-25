
import sys
import re


with open(sys.argv[1]) as f:
    for r in re.finditer(r'(\b(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\b\.){3}\b(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\b', f.read()):
        print(r.group(0))
