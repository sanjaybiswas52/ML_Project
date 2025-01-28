from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dense_rank
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("Second Highest Marks").getOrCreate()

# Define the data
data = [
    (1, 'a', 46),
    (1, 'b', 98),
    (2, 'a', 74),
    (2, 'b', 50),
    (3, 'b', 15),
    (3, 'a', 35),
    (1, 'c', 100),
    (2, 'c', 29),
    (3, 'c', 76)
]

# Define schema
columns = ["student_id", "subject", "marks"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Define a window specification for each subject
windowSpec = Window.partitionBy("subject").orderBy(col("marks").desc())

# Add dense rank column based on marks
df_with_rank = df.withColumn("rank", dense_rank().over(windowSpec))

# Filter rows where rank is 2 (second highest)
second_highest = df_with_rank.filter(col("rank") == 2).select("subject", "marks")

# Show the results
second_highest.show()

# Stop Spark session
spark.stop()