import numpy as np
import matplotlib.pyplot as plt

#data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
data = np.sort(data)[::-1]
print(data)
p50 = np.percentile(data, 50)  # 50th percentile (median)
print(f"50th Percentile (Median): {p50}")

print(f"\nNext Example\n--------------")
percentiles = np.percentile(data, [25, 50, 75])  # Compute Q1, Median, Q3
print(f"25th Percentile (Q1): {percentiles[0]}")
print(f"50th Percentile (Median): {percentiles[1]}")
print(f"75th Percentile (Q3): {percentiles[2]}")

plt.hist(data, 50)
plt.show()
