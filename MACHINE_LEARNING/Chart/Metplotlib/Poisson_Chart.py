#Poisson Probability Mass Function
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

mu = 500
x = np.arange(400, 600, 0.5)
print(x)
plt.plot(x, poisson.pmf(x, mu), alpha=0.5, color='blue')
plt.show()