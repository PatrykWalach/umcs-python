

def string_to_dict(keysValuesString):
    return dict(subString.split(":") for subString in keysValuesString.split(",")) 

print(string_to_dict("k1: v1,k2: v2,k3: v3"))
