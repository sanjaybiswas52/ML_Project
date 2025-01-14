import pandas as pd
import matplotlib.pyplot as plt

def process_file(file_path1, file_path2):
    # Reads two CSV files, processes them by replacing special characters
    # Load the CSV files
    data1 = pd.read_csv(file_path1)
    data2 = pd.read_csv(file_path2)
    data = pd.concat([data1, data2], ignore_index=True)

    # Remove zeros or unwanted values from the output
    df = pd.DataFrame(data, columns=["Symbol","% Chg"])  # Add column name for clarity
    # df = df[df["Symbol"] != 0] # Remove rows with zero
    df = df[~df['Symbol'].str.startswith('NIFTY', na=False)]  # Remove rows with Nifty
    df["Symbol"] = df["Symbol"].astype(str).str.replace(r'[,&\s-]+', '_', regex=True)  # Replace '&' with z'_'
    output_file = df.dropna()  # Drop any rows with NaN values, if present
    return output_file

# Bar Chart Creation
def create_bar_chart(data):
    """
    Creates a bar chart for the given DataFrame if the required columns exist.
    """
    if 'Symbol' in data.columns and '% Chg' in data.columns:
        # Ensure the data is sorted by '% Chg' in descending order
        sorted_data = data.sort_values(by='% Chg', ascending=True)

        # Plot the bar chart
        plt.figure(figsize=(12, 8))
        plt.bar(sorted_data['Symbol'], sorted_data['% Chg'], color='orange', edgecolor='black')

        # Add chart labels and titles
        plt.title('Bar Chart of Symbols and % Change (Biggest to Smallest)', fontsize=16)
        plt.xlabel('Symbol', fontsize=14)
        plt.ylabel('% Change', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.tight_layout()
        plt.show()
    else:
        print("The required columns 'Symbol' and '% Chg' are not present in the dataset.")

# Main process
file_path1= '/Users/sanjaybiswas/Downloads/Chartink_Positive_Hammer, Technical Analysis Scanner.csv'
file_path2 = '/Users/sanjaybiswas/Downloads/Chartink_Gravestone_Doji, Technical Analysis Scanner.csv'

# Reads two CSV files, processes them by replacing special characters
output_file = process_file(file_path1, file_path2)
# Save to the output file
output_file_df = pd.DataFrame(output_file, columns=["Symbol"])
output_file_df.to_csv('/Users/sanjaybiswas/Downloads/Chartink_Gravestone_Hammer_StoKs.txt', index=False)
print(f"Cleaned data saved to {output_file}")

# Example usage of the bar chart function
create_bar_chart(output_file)
