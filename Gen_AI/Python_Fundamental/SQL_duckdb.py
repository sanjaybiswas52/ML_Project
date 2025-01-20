import duckdb
from mylibrary import file_movement as mylib
import pandas as pd

#mylib.convert_to_parquet('/Users/sanjaybiswas/Downloads/csv_files/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner.csv','/Users/sanjaybiswas/Downloads/csv_files/Parquet_file')
#mylib.search_files('/Users/sanjaybiswas/Downloads/csv_files', '.csv')



# SQL query to join Parquet files
query1 = """
SELECT 
    count(*)
FROM 
    '/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet' AS t1
JOIN 
    '/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet' AS t2
ON 
    t1.model = t2.model
"""

rsi_above_70 = pd.read_parquet('/Users/sanjaybiswas/Downloads/csv_files/Parquet_file/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner.parquet')

query2 = """ 
SELECT * FROM "rsi_above_70" t1
WHERE "Stock Name" LIKE '%Ltd%'
"""

query3 = """ 
        SELECT "Stock Name", count(*) as CNT from "rsi_above_70" t1
            GROUP BY "Stock Name" HAVING count(*) > 1 
        """

# Execute the query and save the result
result = duckdb.query(query2).to_df()
#result.to_parquet('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars_output.parquet', index=False)

print(f"{result[:10]}")

