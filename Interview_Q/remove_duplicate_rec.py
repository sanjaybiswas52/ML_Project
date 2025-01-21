def remove_duplicates(input_file):
   
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines() # Read all lines from the input file
            for data in lines:
                print(f" {data}")

        print(f" \n")
        print("*** Use a set to store unique records")
        # Use a set to store unique records
        unique_lines = set(line.strip() for line in lines) # Remove leading/trailing whitespace from each line
        
        #with open(output_file, 'w') as outfile:
        for line in unique_lines:
                #outfile.write(line + '\n')  # Write each unique line to the output file
            print(line)
        
    except Exception as e:
        print(f"Error processing file: {e}")

# Example Usage
input_file = '/Users/sanjaybiswas/Downloads/csv_files/Duplicate_test_data.csv'  # Replace with the path to your input file
remove_duplicates(input_file)
