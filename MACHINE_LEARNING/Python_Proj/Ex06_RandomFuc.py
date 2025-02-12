import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Range between -3 to 3 and difference would be 0.1
list_range = np.arange(-2, 2, 0.1)
print(list_range)
plt.plot(list_range, norm.pdf(list_range))

# Normal : loc = mean default 0 , scale = standard deviation default 1.0
rand_nor = np.random.normal()
print(f" Random Normal : {rand_nor}")

rand_nor = np.random.normal(5.0, 2.0, 10)
print(f" Random Normal : {rand_nor}")
plt.plot(rand_nor, norm.pdf(rand_nor))
plt.show()

rand_uni = np.random.uniform(-10.0, 10.0, 100)
print(f" Random Uniform : {rand_uni}")
'''
samples = np.random.normal(loc=0, scale=1, size=(2, 3))
print(samples)
'''