# %%
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.randint(7,size=(10,10))
unique, counts = np.unique(arr, return_counts=True)

plt.bar(unique, counts)
 
 

# %%
