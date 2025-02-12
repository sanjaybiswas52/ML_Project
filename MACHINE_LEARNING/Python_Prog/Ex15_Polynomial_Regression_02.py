import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(2)

# Generate random data
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

# Split the data into training and testing sets
trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]
trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

# Fit a polynomial to the training data
x = np.array(trainX)
y = np.array(trainY)
p4 = np.poly1d(np.polyfit(x, y, 8))

#Against our test data
testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])

xp = np.linspace(0, 7, 100)

# Create a figure with a custom layout for subplots
fig, axes = plt.subplots(2, 3, figsize=(16, 8))  # 2 rows, 2 columns

# Scatter plot of all data
axes[0, 0].scatter(pageSpeeds, purchaseAmount, color='blue', alpha=0.6)
axes[0, 0].set_title("All Data")
axes[0, 0].set_xlabel("Page Speeds")
axes[0, 0].set_ylabel("Purchase Amount")
axes[0, 0].legend()

# Scatter plot of training data
axes[0, 1].scatter(trainX, trainY, color='green', alpha=0.6)
axes[0, 1].set_title("Training Data")
axes[0, 1].set_xlabel("Page Speeds")
axes[0, 1].set_ylabel("Purchase Amount")
axes[0, 1].legend()

# Scatter plot of testing data
axes[0, 2].scatter(testX, testY, color='red', alpha=0.6)
axes[0, 2].set_title("Testing Data")
axes[0, 2].set_xlabel("Page Speeds")
axes[0, 2].set_ylabel("Purchase Amount")
axes[0, 2].legend()

# Polynomial plot against training data
axes[1, 0].scatter(x, y, color='purple', alpha=0.6, label='Training Data')
axes[1, 0].plot(xp, p4(xp), c='r', label='Polynomial Fit')
axes[1, 0].set_title("Polynomial Fit (Training Data)")
axes[1, 0].set_xlabel("Page Speeds")
axes[1, 0].set_ylabel("Purchase Amount")
axes[1, 0].legend()

# gainst our test data
axes[1, 1].scatter(testx, testy)
axes[1, 1].plot(xp, p4(xp), c='r')
axes[1, 1].set_title("Aainst our test data Data)")
axes[1, 1].set_xlabel("Page Speeds")
axes[1, 1].set_ylabel("Purchase Amount")
axes[1, 1].legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

x = np.array(trainX)
y = np.array(trainY)

p4 = np.poly1d(np.polyfit(x, y, 8))
xp = np.linspace(0, 7, 100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()

testx = np.array(testX)
testy = np.array(testY)

axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(xp, p4(xp), c='r')
plt.show()