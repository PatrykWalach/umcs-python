
import threading
import random
from queue import Queue
import math
import collections


def decompose(x):
    i = 2
    e = math.floor(math.sqrt(x))
    while i <= e:
        while x % i == 0:
            yield i
            x //= i
            e = math.floor(math.sqrt(x))
        i += 1

    if x > 1:
        yield x


def acc_decompose(r):
    return list(collections.Counter(r).items())


q = Queue()


results = [[] for i in range(5)]


def thread_decompose(i):
    for r in decompose(random.getrandbits(64)):
        results[i].append(r)


threads = [threading.Thread(
    target=thread_decompose, name='Decompose-'+str(i), args=(i,)) for i in range(5)]


def print_results():
    print(', '.join(str(acc_decompose(r)) for r in results))


def print_threads():
    global threads_printer

    print_results()

    threads_printer = threading.Timer(1, print_threads)
    threads_printer.name = "Printer"
    threads_printer.start()


threads_printer = threading.Timer(1.0, print_threads)
threads_printer.name = "Printer"
threads_printer.start()

for t in threads:
    t.start()

for t in threads:
    t.join()

threads_printer.cancel()

print_results()