from functools import reduce
import operator


def filter_not_int_args(fn):
    def decorated(*args):
        return fn(*filter(lambda arg: isinstance(arg, int), args))
    return decorated


@filter_not_int_args
def add(*args):
    return sum(args)


@filter_not_int_args
def mul(*args):
    return reduce(operator.mul, args)


print(mul(6, 5))
print(add('12', '75', 3, 4))
