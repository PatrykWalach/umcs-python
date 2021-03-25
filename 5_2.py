
import re


def read(fileName: str, width: int):
    f = open(fileName)

    for l in [r.center(width)
              for r in f.read().replace('\n', '').split(' ')]:
        yield l
    f.close()


for l in read('5_2.txt', 40):
    print(l)
