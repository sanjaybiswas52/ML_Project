import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(9,0.5,10000)
plt.hist(vals,50)
#plt.show()


print(f"The first moment is the mean; this data should average out to about 0:\nThe first moment is Mean value :{np.mean(vals)}")
print(f"The second moment is the variance :{np.var(vals)}")
