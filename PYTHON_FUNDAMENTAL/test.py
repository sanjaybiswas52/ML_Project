from pyspark.sql import SparkSession
from pyspark.sql.functions import col, dense_rank
import pandas as pd
from pyspark.sql.window import Window

sc = SparkSession.builder.master("local").appName("Second Highest Mark").getOrCreate()
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

columns = ["student_id", "subject", "marks"]
df = sc.createDataFrame(data, columns)

partition_data = Window.partitionBy("subject").orderBy(col("marks").desc())

rank = df.withColumn("rank", dense_rank().over(partition_data))
second_highest = rank.filter(col("rank") == 2).select("subject", "marks","rank")

second_highest.show()

"""
input_file = '/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data'
f_rdd = sc.sparkContext.textFile(input_file)
#df = sc.createDataFrame(df)
for data in f_rdd.collect():
    print(f" {data}")

data_rdd = f_rdd.map(lambda line: line.split("\t")) \
                .map(lambda cols: Row(student_id=int(cols[0]), subject=cols[1], marks=int(cols[2])))

# Create a DataFrame from the RDD
df = sc.createDataFrame(data_rdd)

# Show the DataFrame
df.show()

"""

