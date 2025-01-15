import duckdb
from mylibrary import createparquet as mylib

#mylib.convert_to_parquet('/Users/sanjaybiswas/Downloads/Spurts-in-OI-By-Underlying-08012025.csv','/Users/sanjaybiswas/Downloads')

# SQL query to join Parquet files
query = """
SELECT 
    count(*)
FROM 
    '/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet' AS t1
JOIN 
    '/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet' AS t2
ON 
    t1.model = t2.model
"""

# Execute the query and save the result
result = duckdb.query(query).to_df()
#result.to_parquet('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars_output.parquet', index=False)

print(f"{result[:10]}")