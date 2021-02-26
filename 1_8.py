firstList = []
secondList = []

for i in range(ord('a'),ord('f')):
    firstList.append(chr(i))

for i in range(ord('f'),ord('k')):
    secondList.append(chr(i))

def alternateLists():
    global firstList
    global secondList
    alternatedList = [None]*(len(firstList)+len(secondList))
    alternatedList[::2]=firstList
    alternatedList[1::2]=secondList
    return alternatedList

print(alternateLists())
