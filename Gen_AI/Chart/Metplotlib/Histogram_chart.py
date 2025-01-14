import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
print(incomes)
plt.hist(incomes, 50)
plt.show()

