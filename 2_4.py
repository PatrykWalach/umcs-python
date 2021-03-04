
import sys
f=open("plik4.txt")

print(f.readlines()[int(sys.argv[1])])

f.close()