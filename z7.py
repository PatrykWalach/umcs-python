
import numpy as np
import matplotlib.pyplot as plt

mu = 1
sigma = 2
x = np.random.normal(mu, sigma, size=400)
x.sort()
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu)**2 / (2 * sigma**2))

# miejsce na kod:

plt.scatter(x, y,  label='p-plot')

plt.legend()
# koniec
