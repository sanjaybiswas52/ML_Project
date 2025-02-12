from scipy import stats
import numpy as np
from tabulate import tabulate

# Sample data
ages = [21, 25, 21, 25, 21, 10000, 21, 25, 25, 25]
odd_num = [1,2,3,4,5]  # dataset has an odd number of values
even_num = [1,2,3,5,6,7]  # dataset has an even number of values

# Calculate statistics for each dataset
ages_mode = stats.mode(ages)
odd_mode = stats.mode(odd_num)
even_mode = stats.mode(even_num)

print(ages_mode)
# Print the mode and its frequency
# For older versions of SciPy (scalar output)
try:
    print("Mode:", ages_mode.mode[0])
    print("Frequency:", ages_mode.count[0])
except IndexError:  # Handle scalar values
    print("Except Mode:", ages_mode.mode)
    print("Except Frequency:", ages_mode.count)

print(f"\nOdd Number - Mean : {np.mean(odd_num)}     \nEven Number - Mean : {np.mean(even_num)}")
print(f"\nOdd Number - Median : {np.median(odd_num)}     \nEven Number - Median : {np.median(even_num)}")

print(f"\nOdd Number - Mode : {stats.mode(odd_num)}")
print(f"\nEven Number - Mode : {stats.mode(even_num)}")

print("Odd Number Mode:", odd_mode.mode)
print("Odd Number Frequency:", odd_mode.count)
print("Even Number Mode:", even_mode.mode)
print("Even Number Frequency:", even_mode.count)

# Create a table for results
data = [
    [ages, np.mean(ages), np.median(ages), ages_mode.mode, ages_mode.count, len(ages), "Ages -Categorical :value that occurs most frequently in a dataset.\nMedian- Sort the list than Find the Middle Value(s) \n   [21, 21, 21, 21, 25, 25, 25, 25, 25, 10000]\n   Median = (5th value + 6th value) /2 = (25 + 25)/2= 25\nMode- Most Frequent value in list"],
    [odd_num, np.mean(odd_num), np.median(odd_num), odd_mode.mode, odd_mode.count, len(odd_num),"Odd - Unique values with odd in numbers" ],
    [even_num, np.mean(even_num), np.median(even_num), even_mode.mode, even_mode.count, len(even_num), "Even - Unique values with Even in numbers\nMean = Sum of Numbers/Count =24/6 = 4"]
]

# Headers for the table
headers = ["Dataset", "Mean", "Median", "Mode", "Frequency", "Count","Comment"]

# Print the table
print(tabulate(data, headers=headers, tablefmt="grid"))