import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to load CSV files
def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        exit()
    except Exception as e:
        print(f"Error reading the file {file_path}: {e}")
        exit()

def create_bar_chart(data):
    # Check if required columns exist
    if 'Symbol' in data.columns and '% Chg_x' in data.columns:
        # Define bar colors based on % Chg values
        colors = ['green' if val >= 0 else 'red' for val in data['% Chg_x']]

        # Create the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(data['Symbol'], data['% Chg_x'], color=colors)

        # Add titles and labels
        plt.title('Bar Chart of New Stocks (% Change)', fontsize=14)
        plt.xlabel('Symbol', fontsize=12)
        plt.ylabel('% Change', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()  # Adjust layout to avoid clipping

        # Show the plot
        plt.show()
    else:
        print("The required columns 'Symbol' and '% Chg' are not present for the bar chart.")

# File paths (modify as needed)
curr_above70 = '/Users/sanjaybiswas/Downloads/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner (1).csv'  # Replace with your current file path
prev_above70 = '/Users/sanjaybiswas/Downloads/ChartInk_RSI_above_70_MonthlyWeekly_Timeframe, Technical Analysis Scanner.csv'  # Replace with your previous file path

# Load the files
data_c = load_csv(curr_above70)
data_p = load_csv(prev_above70)

# Specify the column to compare
key_column = 'Symbol'

# Merge files on the specified column
merged = pd.merge(data_c, data_p, on=key_column, how='outer', indicator=True)

# Separate results
left_file_only = merged[merged['_merge'] == 'left_only'].copy()  # Use `.copy()` to explicitly create a copy

# Print new stocks
print("\nNew Stocks added in whose RSI is above 70")
print(f"{'Symbol':<10} {'Stock Name':<30}")
print("-" * 40)
for _, row in left_file_only.iterrows():
    print(f"{row['Symbol']:<10} {row['Stock Name_x']:<30}")

# Save new stocks to a CSV
columns_to_print = ['Symbol']  # Adjust columns as needed
try:
    current_date = datetime.now().strftime('%Y-%m-%d')
    output_path = f"/Users/sanjaybiswas/Downloads/RSI_70above_{current_date}.txt"
    left_file_only[columns_to_print].to_csv(output_path, index=False)
    print(f"\nNew stocks file saved to: {output_path}")
except Exception as e:
    print(f"Error saving the output file: {e}")

# Remove '%' and Convert '% Chg_x' to numeric using .loc
left_file_only.loc[:, '% Chg_x'] = left_file_only['% Chg_x'].str.replace('%', '', regex=False)
left_file_only.loc[:, '% Chg_x'] = pd.to_numeric(left_file_only['% Chg_x'], errors='coerce')

# Drop rows with NaN values in '% Chg_x'
data = left_file_only.dropna(subset=['% Chg_x'])

# Sort data by '% Chg_x' in descending order
data = data.sort_values(by='% Chg_x', ascending=False)

# Example usage of the bar chart function
print(data[['Symbol', '% Chg_x']])

# Create the bar chart with the sorted data
create_bar_chart(data)