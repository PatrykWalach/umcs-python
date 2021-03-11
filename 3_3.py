def filter(predicate, list):
    return [l for l in list if predicate(l)]


def predicate(n):
    return n % 7 == 0 and n % 3 == 0


print(filter(predicate, range(0, 1000)))
