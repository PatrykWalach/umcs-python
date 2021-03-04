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


print(encode("jakisciagznakow"))

print(decode(encode("jakisciagznakow")))