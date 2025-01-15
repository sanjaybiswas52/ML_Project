'''
import numpy as ny
import tensorflow as tf
import pandas as pd

dataset = pd.read_csv('/Users/sanjaybiswas/Downloads/Spurts-in-OI-By-Underlying-21122024.csv')
#dataset = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/Deep Learning A-Z/Part 1 - Artificial Neural Networks (ANN)/Churn_Modelling.csv')
X = dataset.iloc[:, 3:-1].values
print(X)

col_x = X.shape[1]
print(f" --- The CSV file has {col_x} columns.")

columns = X.columns.tolist()
print("Columns in the CSV file:")
for col in columns:
    print(col)
'''
import pandas as pd
import numpy as np

# Example of loading a NumPy array
array = np.array([[1, 'Sanjay', 'M'], [2, 'Ajay', 'M'],[3, 'Varsha', 'F']])  # Example data
# Convert to DataFrame with column names
data = pd.DataFrame(array, columns=['ROLL', 'ST_NAME', 'GENDER'])
print(data)
# Display column names
print("")
print("Columns in the DataFrame:")
print(data.columns.tolist())

print("")
X = data.iloc[:, 0:-1].columns
print("Selected columns only")
print(X)

print("")
X = data.iloc[:, 0:-1].values
print("Selected Values only")
print(X)

print("")
Y = data.iloc[:, -1].values
print("Selected Last record only")
print(Y)