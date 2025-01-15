import pandas as pd
import numpy as np
import subprocess
import matplotlib.pyplot as plt

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

#df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df = pd.read_parquet('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet')

df1=df[['Mileage','Price']]
bins =  np.arange(0,50000,10000)
print(df1['Mileage'][:10])
print(bins)

print(pd.cut(df1['Mileage'],bins))

'''
groups = df1.groupby(pd.cut(df1['Mileage'],bins)).mean()
print(groups.head())
groups['Price'].plot.line()
plt.show()
'''