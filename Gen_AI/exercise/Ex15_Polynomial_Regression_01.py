from pylab import *
import numpy as np
from scipy import stats
import subprocess

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

np.random.seed(2)
mean = 3.0
std_dev = 1.0
pageSpeeds = np.random.normal(mean, std_dev, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
print(f"\npageSpeeds :{pageSpeeds[:10]} \n\npurchaseAmount :{purchaseAmount[:10]}\n")

scatter(pageSpeeds, purchaseAmount)
plt.show()
'''
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.poly1d(np.polyfit(x, y, 4))

xp = np.linspace(0, 7, 100)
print(f"\npoly1d :{p4} \n\nlinespace(linspace)  : {xp[:10]}\n\n")
plt.scatter(x, y, label='Actual Data')
plt.plot(xp, p4(xp), c='r', label='Polynomial Regression Line')
plt.xlabel("X (PageSpeeds)")
plt.ylabel("y (PurchaseAmount)")
plt.legend()
plt.show()
'''