## Binomial Probability Mass Function
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
print(x)
plt.plot(x, binom.pmf(x, n, p))
plt.show()