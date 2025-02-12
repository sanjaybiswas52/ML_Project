import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from tabulate import tabulate

#Then, compute the mean (average) - it should be close to 27,000:
incomes = np.random.normal(27000, 15000, 10)
print(f"Income : {incomes}\n")
# Print the table
data = [incomes]
header = ["random.normal"]
print(tabulate(data, headers=header, tablefmt="grid"))


even_mode = stats.mode(incomes)
print("Even Number Frequency:", even_mode.count)
print("Even Number Count:", len(even_mode))


print(f"\nMean : {np.mean(incomes)}")
print(f"Median : {np.median(incomes)}")

#We can segment the income data into 50 buckets, and plot it as a histogram:
#plt.hist(incomes,50)
#plt.show()

print(f"\nAppend 100000000 in Income")
incomes = np.append(incomes, [100000000])
print(f"Income : {incomes}")
print(f"Mean : {np.mean(incomes)}")
print(f"Median : {np.median(incomes)}")


#Mode
#Next, let's generate some fake age data for 500 people:
print(f"\nUse in Large data set")
ages = np.random.randint(18, high=90, size= 500)
print(ages)

print(f" Stats : {stats.mode(ages)}")
ages_mode = stats.mode(ages)
print(f" Mode: {ages_mode.mode},  Frequency: {ages_mode.count}")
print(f" Mean : {np.mean(ages)}")
print(f" Median : {np.median(ages)}")