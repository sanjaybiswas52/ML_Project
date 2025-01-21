import os
from datetime import datetime

"""
print(datetime.strptime('06-Jan-2025', '%d-%b-%Y').strftime('%d-%b-%Y'))
date_object = datetime.strptime('06-Jan-2025', '%d-%b-%Y')
print(date_object.strftime('%d-%b-%Y'))


filename = '/Users/sanjaybiswas/Downloads/csv_files/T20_GL_gainers_NIFTY_14-Jan-2025.csv'
parts = filename.split('_')
print(len(parts))
print(parts[-1].split(".")[0].split("-"))


if len(parts) >= 3:
    day, month, year = parts[-1].split(".")[0].split("-")  # Split and extract components
    date_str = f"{day}-{month}-{year}"
    print(date_str)
    parsed_date = datetime.strptime(date_str, '%d-%b-%Y')  # Parse the date
    parsed_date.strftime('%Y-%m-%d')  # Return in 'yyyy-mm-dd' format
    print(parsed_date.strftime('%Y-%m-%d') )

    """
import os
from datetime import datetime

def extract_date_from_filename(filename):
    try:
        # Handle "dd-MMM-yyyy" format (e.g., "14-Jan-2025")
        if '-' in filename:
            # Extract the last portion that looks like a date
            possible_date = filename.split('_')[-1].split('.')[0]  # Split on underscore and remove the file extension
            print("Possible Date: " + possible_date)
            
            # Parse the date
            parsed_date = datetime.strptime(possible_date, '%d-%b-%Y')  
            print("Parsed Date: " + str(parsed_date))
            
            # Return in 'yyyy-mm-dd' format
            return parsed_date.strftime('%Y-%m-%d')  

        return 'unknown'  # Return 'unknown' if no valid date is found
    except Exception as e:
        print(f"Error parsing date from filename '{filename}': {e}")
        return 'unknown'
    
# Test Cases

filenames = [
    "14-Jan-2025.csv",  # Numeric date
    "T20_GL_gainers_NIFTY_14-Jan-2025.csv",  # Named month date
    "summary_report.csv"  # No recognizable date
]

for filename in filenames:
    print(f"Filename: {filename}, Extracted Date: {extract_date_from_filename(filename)}")