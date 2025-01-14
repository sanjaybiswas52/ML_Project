import numpy as np
from pylab import *
import subprocess
from scipy import stats

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

mean = 3.0
std_dev = 1.0
pageSpeeds = np.random.normal(mean, std_dev, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

scatter(pageSpeeds, purchaseAmount)
# Add a vertical line for the mean
#plt.axvline(mean, color='blue', linestyle='dashed', linewidth=2, label="Mean")
plt.show()
print(f"\npageSpeeds :{pageSpeeds[:10]} \n\npurchaseAmount :{purchaseAmount[:10]} ")

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
#print(f"\nLinear Regression : {stats.linregress(pageSpeeds, purchaseAmount)}")
print(f"\nslop     :{slope} \nintercep :{intercept} \nrv_alue  :{r_value} \np_value  : {p_value} \nstd_err  :{std_err}\n")

def predict(x):
    return slope * x + intercept

fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount,label='Actual Data')
plt.plot(pageSpeeds, fitLine, c='r', label='Linear Regression Line')
plt.title("Linear Regression Example")
plt.xlabel("X (PageSpeeds)")
plt.ylabel("y (PurchaseAmount)")
plt.legend()
plt.show()
print(f"fitline :{fitLine[:10]}\n")

