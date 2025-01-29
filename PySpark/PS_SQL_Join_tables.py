from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dense_rank, date_format, to_date, when
import pandas as pd

# Initialize Spark Session
spark = SparkSession.builder.master("local").appName("Query Builder").getOrCreate()

# Define the CSV file paths
data_emp = "/Users/sanjaybiswas/Downloads/csv_files/employee.csv"
output_csv = "/Users/sanjaybiswas/Downloads/csv_files/employee_transformed.csv"
output_excel = "/Users/sanjaybiswas/Downloads/csv_files/employee_filtered.xlsx"
data_dept = "/Users/sanjaybiswas/Downloads/csv_files/departments.csv"
data_location = "/Users/sanjaybiswas/Downloads/csv_files/locations.csv"

# Read the employee data CSV into a DataFrame
df_emp = spark.read.option("header", True).option("inferSchema", True).csv(data_emp)

# Read the department data CSV into a DataFrame
df_dept = spark.read.option("header", True).option("inferSchema", True).csv(data_dept)

# Read the locations data CSV into a DataFrame
df_location = spark.read.option("header", True).option("inferSchema", True).csv(data_location)

# Show DataFrame Schema for employee data
df_emp.printSchema()

# Assuming the date column is named "hire_date", convert it to "dd-MM-yyyy"
df_emp = df_emp.withColumn(
    "hire_date",
    when(
        col("hire_date").rlike(r"^\d{2}-[A-Z]{3}-\d{4}$"),  # Matches "17-JUN-1987"
        date_format(to_date(col("hire_date"), "dd-MMM-yyyy"), "dd-MM-yyyy")  # Convert to "17-06-1987"
    ).otherwise(col("hire_date"))  # Keep other formats unchanged
)

# Join the employee DataFrame with the department DataFrame on 'department_id'
df_emp_dept = df_emp.join(df_dept, df_emp["department_id"] == df_dept["department_id"], "left") \
                    .select(df_emp["*"], df_dept["department_name"],"location_id")

# Now, join the department DataFrame with the locations DataFrame on 'location_id' to add 'city' column
df_emp_dept_location = df_emp_dept.join(df_location, df_emp_dept["location_id"] == df_location["location_id"], "left") \
                                  .select(df_emp_dept["*"], df_location["city"])

# Read the locations data CSV into a DataFrame
df_location = spark.read.option("header", True).option("inferSchema", True).csv(data_location)

# Show the resulting DataFrame with city
df_emp_dept_location.show()

# Write the transformed DataFrame with department and city names to a new CSV file
df_emp_dept_location.write.mode("overwrite").option("header", True).csv(output_csv)

# **Filter data where job_id is "IT_PROG"**
df_emp_IT = df_emp_dept_location.filter(col("job_id") == "IT_PROG")

# Show filtered result
df_emp_IT.show()

# Optionally, write the filtered data to Excel (using pandas)
df_emp_IT_pandas = df_emp_IT.toPandas()
df_emp_IT_pandas.to_excel(output_excel, index=False, engine="openpyxl")

print(f"Filtered data written to Excel: {output_excel}")