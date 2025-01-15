import pandas as pd
import os
from PyPDF2 import PdfReader

# Define a fixed output directory
OUTPUT_DIR = "output_files"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)


input_file = "http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls"
    
output_file = os.path.splitext(input_file)[0] + ".parquet"

file_extension = os.path.splitext(input_file)[1].lower()
base_name = os.path.splitext(os.path.basename(input_file))[0]  # Extract the file name without extension
output_file = os.path.join(OUTPUT_DIR, f"{base_name}.parquet")

print(base_name)