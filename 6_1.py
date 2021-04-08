import math


def sqrt():
    try:
        n = input()
        print(math.sqrt(float(n)))
    except ValueError:
        print('ValueError')

if __name__ == '__main__':
    sqrt()  