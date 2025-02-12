import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
from scipy.stats import binom
# Example data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# 1. Create a histogram
plt.figure(figsize=(8, 5))  # Create a figure for the histogram
plt.hist(data, bins=5, edgecolor='black', color='skyblue', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# 2. Exponential PDF
# Generate exponential data for the same range
x = np.linspace(min(data), max(data), 100)  # Generate points for the line
pdf_values = expon.pdf(x)  # Compute the exponential PDF

plt.figure(figsize=(8, 5))  # Create a figure for the PDF
plt.plot(x, pdf_values, color='red', label='Exponential PDF', linewidth=2)
plt.title('Exponential Probability Density Function')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(axis='both', linestyle='--', alpha=0.6)
plt.show()

#Binomial Probability Mass Function
plt.plot(data, binom.pmf(data, 10, 0.5))
plt.show()