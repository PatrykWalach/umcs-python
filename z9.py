import threading
import time
import queue
import random


def fun1():
    start = time.time()
    licz = random.randrange(1000000, 2000000)
    n = licz
    while n:
        n -= 1
    end = time.time()
    return licz, end-start

# miejsce na kod:


que = queue.Queue(maxsize=10)


for r in range(10):
    t = threading.Thread(target=lambda: que.put(fun1()))
    print(f"t{r} started")
    t.start()


# koniec

while not que.full():
    time.sleep(1)
    print('threads are working...')

while que.qsize():
    print(que.get())
