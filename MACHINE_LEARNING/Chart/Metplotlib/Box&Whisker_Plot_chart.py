import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import  stats

uniformskewed = np.random.rand(100)  * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformskewed, high_outliers, low_outliers))
mean_val = stats.mode(data)

print(f" Data : {data}")
print(f" Max value : {max(data)}")
print(f" Min value : {min(data)}")
print(f" Mean value : {np.mean(data)}")
print(f" Median value : {np.median(data)}")
#print(f" Mode value : {stats.mode(data)}")
print(f" Mode & Frequency value : {mean_val.mode}\n Frequency :{mean_val.count}")

plt.boxplot(data)
plt.show()

print(f" \nAfter shorting Data\n-------------")
data = np.sort(data)
#print(f" Data : {data}")
print(f" Max value : {max(data)}")
print(f" Min value : {min(data)}")
print(f" Mean value : {np.mean(data)}")
print(f" Median value : {np.median(data)}")
#print(f" Mode value : {stats.mode(data)}")
print(f" Mode value : {mean_val.mode}\n Frequency :{mean_val.count}")