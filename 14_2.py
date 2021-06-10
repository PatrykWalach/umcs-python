import threading
import time
from functools import lru_cache


def count(r):
    i = 0
    while(i < r):
        i += 1
    return i

startTime = time.time()
count(66664960)
executionTime = (time.time() - startTime)
print('Not threaded execution time in seconds: ' + str(executionTime))

startTime = time.time()
t1 = threading.Thread(target=count, args=(66664960/2,))
t2 = threading.Thread(target=count, args=(66664960/2,))
t1.start()
t2.start()
t1.join()
t2.join()
executionTime = (time.time() - startTime)
print('Threaded execution time in seconds: ' + str(executionTime))
