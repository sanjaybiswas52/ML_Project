import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(2)

# Generate random data
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

# Split the data into training and testing sets
# 80% of the data will be used for training and 20% for testing
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

# 20% of the data will be used for testing
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Scatter plot of all data
axes[0].scatter(pageSpeeds, purchaseAmount, color='blue', alpha=0.6)
axes[0].set_title("All Data")
axes[0].set_xlabel("Page Speeds")
axes[0].set_ylabel("Purchase Amount")

# Scatter plot of training data
axes[1].scatter(trainX, trainY, color='green', alpha=0.6)
axes[1].set_title("Training Data")
axes[1].set_xlabel("Page Speeds")
axes[1].set_ylabel("Purchase Amount")

# Scatter plot of testing data
axes[2].scatter(testX, testY, color='red', alpha=0.6)
axes[2].set_title("Testing Data")
axes[2].set_xlabel("Page Speeds")
axes[2].set_ylabel("Purchase Amount")

# Adjust layout and show the figure
plt.tight_layout()
plt.show()