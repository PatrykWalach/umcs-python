
import numpy as np


arr = np.array(range(1,26)).reshape((5,5))

print(arr)

reversed_rows = np.flipud(arr)

print(reversed_rows)

reversed_cols = np.fliplr(arr)

print(reversed_cols)

reversed_both = np.flip(arr)

print(reversed_both)