import pandas as pd

#df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')
df = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/PastHires.csv')
df.to_parquet('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/PastHire.parquet', index=False)