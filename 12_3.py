# %%
import matplotlib.pyplot as plt
import numpy as np
import re

with open("plik.txt") as f:
    text = f.read()

arr = np.array(list(re.sub(r'\W|\d','',text)))
unique, counts = np.unique(arr, return_counts=True)

plt.bar(unique, counts)


# %%
