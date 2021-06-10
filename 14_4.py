from queue import Queue

import random
import threading


def fun_count():
    r = random.getrandbits(24)
    i = 0
    while(i < r):
        i += 1
    return i


 


q = Queue()

threads = [threading.Thread(target=lambda: q.put(
    fun_count()), name='FunCount-'+str(r)) for r in range(10)]


def print_threads():
    global threads_printer

    print(', '.join(t.name for t in threading.enumerate()))

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

print(list(q.queue))
