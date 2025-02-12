from pyspark.sql import SparkSession
import multiprocessing

multiprocessing.set_start_method("spawn", force=True)

def remove_duplicates_pyspark(input_file):
    try:
        # Initialize a SparkSession
        spark = SparkSession.builder.appName("RemoveDuplicates").getOrCreate()
        
        # Read the input file as an RDD
        lines_rdd = spark.sparkContext.textFile(input_file)
        
        print("Reading lines from the file:")
        for data in lines_rdd.collect():
            print(f" {data}")
        
        print("\n*** Use RDD transformation to store unique records")
        
        # Use RDD's distinct transformation to remove duplicates
        unique_lines_rdd = lines_rdd.distinct()
        
        # Print the unique lines
        print("Unique lines:")
        for line in unique_lines_rdd.collect():
            print(line)
        
        # Stop the SparkSession
        spark.stop()
    
    except Exception as e:
        print(f"Error processing file: {e}")

# Example Usage
input_file = '/Users/sanjaybiswas/Downloads/csv_files/Duplicate_test_data.csv'  # Replace with the path to your input file
remove_duplicates_pyspark(input_file)