import sqlite3
import pandas as pd

# File paths
file1 = '/Users/sanjaybiswas/Downloads/T20-GL-loosers-NIFTY-15-Jan-2025.csv'  # Replace with your first CSV file path
file2 = '/Users/sanjaybiswas/Downloads/T20-GL-gainers-NIFTY-15-Jan-2025.csv'  # Replace with your second CSV file path

# Load CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Load DataFrames into the database as tables
df1.to_sql('table1', conn, index=False, if_exists='replace')
df2.to_sql('table2', conn, index=False, if_exists='replace')

# SQL query to perform an INNER JOIN on the 'id' column
query = """
SELECT 'looser', t1.Symbol, t1.'%chng'
FROM 
    table1 t1
union
SELECT 'gainer', t2.Symbol, t2.'%chng'
FROM 
    table1 t2
"""

# Execute the query and fetch the result
result = pd.read_sql_query(query, conn)

# Display the result
print("Joined Data:")
print(result)