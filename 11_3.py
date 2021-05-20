
import numpy as np

arr = np.random.randint(101, size=(10, 10))

print(arr)

mapped = np.array(
    [0 if x < 25 or x > 75 else x for x in arr.flat]).reshape(arr.shape)

print(mapped)
