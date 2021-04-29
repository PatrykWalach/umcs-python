from functools import reduce, partial
import operator

calls = 0


def tracked(fn):
    def decorated(*args):
        global calls
        calls += 1
        return fn(*args)
    return decorated


@tracked
def add(*args):
    return sum(args)


@tracked
def mul(*args):
    return reduce(operator.mul, args)


for i in range(10):
    add(i, 1)
    for j in range(10):
        mul(i, j)

print(calls)
