#from mylibrary.file_movement import convert_to_parquet
import pandas as pd

#convert_to_parquet("/Users/sanjaybiswas/Downloads/T20-GL-gainers-NIFTY-31-Jan-2025.csv","/Users/sanjaybiswas/Downloads/Pycharm/data")
df = pd.read_csv("/Users/sanjaybiswas/Downloads/T20-GL-gainers-NIFTY-31-Jan-2025.csv")

# Convert CSV to Parquet
df.to_parquet("/Users/sanjaybiswas/Downloads/Pycharm/data/T20-GL-gainers-NIFTY-31-Jan-2025.parquet", index=False)
