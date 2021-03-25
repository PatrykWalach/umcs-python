
import re


def read(fileName: str, width: int):
    f = open(fileName)

    for l in [r.group(0)
              for r in re.finditer('.{0,'+str(width)+'}', f.read().replace('\n', ''))]:
        yield l
    f.close()


for l in read('5_1.txt', 2):
    print(l)
