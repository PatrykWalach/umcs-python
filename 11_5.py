
import numpy as np

arr = np.random.randint(7, size=(10, 10))

print(arr)

unique, counts = np.unique(arr, return_counts=True)

print(unique)


print(counts)
