import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Define the mean and standard deviation
mean = 0
std_dev = 1

# Generate a range of x values
x = np.linspace(-4, 4, 100)

# Calculate the PDF
pdf_values = norm.pdf(x, loc=mean, scale=std_dev)

# Plot the PDF
plt.figure(figsize=(8, 5))
plt.plot(x, pdf_values, color='red', label="Normal Distribution (Mean=0, Std=1)")
plt.title("Normal Probability Density Function")
plt.xlabel("x")
plt.ylabel("Density")

legend = plt.legend()
for text in legend.get_texts():
    text.set_color("blue")  # Set the color of the labels in the legend to red

plt.grid(alpha=0.4)
plt.hist(x, bins=30, density=True, alpha=0.9, color='green', label="Histogram of Samples")
plt.show()