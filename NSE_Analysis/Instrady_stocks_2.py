import pandas as pd
import matplotlib.pyplot as plt

# Define file paths for CSV data processed by both scripts
file1_path = "/Users/sanjaybiswas/Downloads/Spurts-in-OI-By-Underlying-15122024.csv"
file2_path = "/Users/sanjaybiswas/Downloads/T20-GL-gainers-NIFTY-15-Dec-2024.csv"

# Load the datasets
try:
    data1 = pd.read_csv(file1_path)
    data2 = pd.read_csv(file2_path)
except Exception as e:
    print(f"Error loading files: {e}")
    exit()

# Process data as per previous logic for both scripts
if 'Symbol' in data1.columns and 'Symbol' in data2.columns:
    # Merge data by symbol for a combined chart
    merged_data = pd.merge(data1, data2, on='Symbol', how='inner')

    # Filter and sort data based on %chng in OI
    filtered_data = merged_data[merged_data['%chng'] > 2.0]
    top10 = filtered_data.nlargest(10, '%chng in OI')

    # Prepare data for bar chart
    symbols = top10['Symbol']
    oi_values = top10['%chng in OI']
    oi_values_script1 = top10['%chng in OI_x']  # From first script
    oi_values_script2 = top10['%chng in OI_y']  # From second script

    # Plot bar chart
    bar_width = 0.35  # Bar width for side-by-side bars
    x = range(len(symbols))  # X positions

    plt.figure(figsize=(12, 6))
    plt.bar(x, oi_values_script1, bar_width, label='Script 1', color='blue')
    plt.bar([p + bar_width for p in x], oi_values_script2, bar_width, label='Script 2', color='orange')

    # Add labels and title
    plt.xlabel('Symbols', fontsize=12)
    plt.ylabel('% Change in Open Interest', fontsize=12)
    plt.title('Comparison of % Change in Open Interest', fontsize=14)
    plt.xticks([p + bar_width / 2 for p in x], symbols, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    # Show the plot
    plt.show()
else:
    print("Required columns ('symbol') not found in one or both datasets.")