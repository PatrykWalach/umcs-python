from queue import Queue

import random
import threading


def fun_count():
    r = random.getrandbits(24)
    i = 0
    while(i < r):
        i += 1
    return i


fun_count()


q = Queue()

threads = [threading.Thread(target=lambda q: q.put(
    fun_count()), name=str(r), args=(q,)) for r in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

l = []
while not q.empty():
    l.append(q.get())

print(l)
