def fib(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fib(n - 1) + fib(n - 2)


n = int(float(input()))

print([fib(x) for x in range(n)])
