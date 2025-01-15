import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

# Generate random numbers from a normal distribution
mean = 5.0
std_dev = 2.0
data = np.random.normal(loc=mean, scale=std_dev, size=1000)
print(f"Data : {data[:10]} \n\nMin value :{min(data)}   \nMax value : {max(data)} \nMean value :{np.mean(data)} \
      \nDeviation value :{np.std(data)}")

