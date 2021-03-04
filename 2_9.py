import sys
KEY = 3
    
def encode(txt):
    encoded = ''
    for char in txt: 
        encoded += chr((ord(char) + KEY - 97) % 26 + 97)
    return encoded

def decode(txt):
    decoded = ""
    for char in txt:
        decoded += chr((ord(char) - KEY - 97) % 26 + 97)
    return decoded


with open(sys.argv[1]) as r:
    with open(sys.argv[2],"w") as w:
        w.write(encode(r.read()))