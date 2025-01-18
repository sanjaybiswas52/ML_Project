import pandas as pd
import os
from PyPDF2 import PdfReader
import subprocess

def convert_to_parquet(input_file, OUTPUT_DIR):
    # Execute a terminal command fro clear screen
    print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

    # Define a fixed output directory
    #OUTPUT_DIR = "/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file"

    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    """
    Converts input file of various formats to Parquet format and saves it to a fixed directory.
    """
    file_extension = os.path.splitext(input_file)[1].lower()
    base_name = os.path.splitext(os.path.basename(input_file))[0]  # Extract the file name without extension
    output_file = os.path.join(OUTPUT_DIR, f"{base_name}.parquet")
    
    try:
        if file_extension == ".csv":
            # Read CSV and write to Parquet
            df = pd.read_csv(input_file)
            df.to_parquet(output_file, index=False)
            print(f"Converted CSV to Parquet: {output_file}")
        
        elif file_extension in [".xls", ".xlsx"]:
            # Read Excel and write to Parquet
            df = pd.read_excel(input_file)
            df.to_parquet(output_file, index=False)
            print(f"Converted Excel to Parquet: {output_file}")
        
        elif file_extension == ".txt":
            # Read Text (assumes tabular data with a delimiter)
            df = pd.read_csv(input_file, delimiter="\t")
            df.to_parquet(output_file, index=False)
            print(f"Converted Text to Parquet: {output_file}")
        
        elif file_extension == ".json":
            # Read JSON and write to Parquet
            df = pd.read_json(input_file)
            df.to_parquet(output_file, index=False)
            print(f"Converted JSON to Parquet: {output_file}")
        
        elif file_extension == ".pdf":
            # Extract text from PDF and save to Parquet (not tabular)
            reader = PdfReader(input_file)
            text = "\n".join([page.extract_text() for page in reader.pages])
            df = pd.DataFrame({'Text': [text]})
            df.to_parquet(output_file, index=False)
            print(f"Converted PDF text to Parquet: {output_file}")
        
        else:
            print(f"Unsupported file format: {file_extension}")
    
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

'''
# Example Usage
if __name__ == "__main__":
    input_files = [
        "/Users/sanjaybiswas/Downloads/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner (3).csv",  # Replace with your CSV file path
        "http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls"
    ]
    
    for input_file in input_files:'
    input_file = "/Users/sanjaybiswas/Downloads/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner (2).csv"
    convert_to_parquet(input_file)

'''   
import sys
sys.path.append('/Users/sanjaybiswas/Documents/Pycharm/pythonProject/sanjay/lib/python3.12/site-packages/mylibrary')

import mylibrary
