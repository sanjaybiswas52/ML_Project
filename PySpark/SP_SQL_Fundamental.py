from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dense_rank, date_format, to_date, when
import pandas as pd

# Initialize Spark Session
spark = SparkSession.builder.master("local").appName("Query Builder").getOrCreate()

# Define the CSV file path
data_emp = "/Users/sanjaybiswas/Downloads/csv_files/employee.csv"
output_csv = "/Users/sanjaybiswas/Downloads/csv_files/employee_transformed.csv"
output_excel = "/Users/sanjaybiswas/Downloads/csv_files/employee_filtered.xlsx"
data_dept = "/Users/sanjaybiswas/Downloads/csv_files/departments.csv"

# Read the CSV file into a DataFrame
df_emp = spark.read.option("header", True).option("inferSchema", True).csv(data_emp)

# Show DataFrame Schema and Data
df_emp.printSchema()

# Assuming the date column is named "joining_date", convert it to "dd-MM-yyyy"
#df_emp = df_emp.withColumn("hire_date", date_format(to_date(col("hire_date"), "dd-MMM-yyyy"), "dd-MM-yyyy"))
df_emp = df_emp.withColumn(
    "hire_date",
    when(
        col("hire_date").rlike(r"^\d{2}-[A-Z]{3}-\d{4}$"),  # Matches "17-JUN-1987"
        date_format(to_date(col("hire_date"), "dd-MMM-yyyy"), "dd-MM-yyyy")  # Convert to "17-06-1987"
    ).otherwise(col("hire_date"))  # Keep other formats unchanged
)

# Write the transformed DataFrame to a new CSV file
df_emp.write.mode("overwrite").option("header", True).csv(output_csv)

# **Filter data where job_id is "IT_PROG"**
df_emp_IT= df_emp.filter(col("job_id") == "IT_PROG")

# Convert PySpark DataFrame to Pandas DataFrame
df_emp_pandas = df_emp_IT.toPandas()

# Write to Excel file
#df_emp_pandas.to_excel(output_excel, sheet_name="employee" ,index=False, engine="openpyxl")
with pd.ExcelWriter(output_excel, mode='a', engine='openpyxl') as writer:
    df_emp_pandas.to_excel(writer, sheet_name='IT_PROG')
print(f"Transformed data successfully written to: {output_csv}")