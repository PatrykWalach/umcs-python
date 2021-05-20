# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Funckje sin/cos')


plt.scatter(x, np.sin(x))
plt.scatter(x, np.cos(x))

plt.legend(["sin(x)","cos(x)"])

# %%
