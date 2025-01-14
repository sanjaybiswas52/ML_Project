import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Calculate yesterday's date
yesterday = datetime.today() - timedelta(days=0)
last_date = yesterday.strftime('%d%m%Y')
print(f"Last Date: {last_date}")

current_date = datetime.now().strftime('%d%m%Y')
file_path = f"/Users/sanjaybiswas/Downloads/Spurts-in-OI-By-Underlying-{last_date}.csv"

data = pd.read_csv(file_path)

# Display the first few rows to understand the data structure
print(data.head())
print(data.columns.tolist())

# Ensure the required columns exist
if 'Symbol' in data.columns and '%chng in OI' in data.columns:
    # Exclude the symbol "NIFTY"
    filtered_data = data[~data['Symbol'].str.contains('NIFTY', case=False, na=False)]

    # Sort data by "%chng in OI" in descending and ascending order
    top10 = filtered_data.nlargest(10, '%chng in OI')  # Top 10 largest
    bottom10 = filtered_data.nsmallest(10, '%chng in OI')  # Top 10 smallest

    # Combine the two datasets
    combined_data = pd.concat([top10, bottom10])

    # Create a single bar chart
    plt.figure(figsize=(12, 8))
    colors = ['seagreen' if x in top10['Symbol'].values else 'tomato' for x in combined_data['Symbol']]
    plt.bar(combined_data['Symbol'], combined_data['%chng in OI'], color=colors, edgecolor='black')

    # Add titles and labels
    plt.title('Top 10 and Bottom 10 NSE Stocks by % Change in Open Interest', fontsize=16)
    plt.xlabel('STOCKS', fontsize=14)
    plt.ylabel('% Change in Open Interest', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()

    # Add a legend
    plt.legend(['Top 10', 'Bottom 10'], loc='upper right', fontsize=12)

    # Show the chart
    plt.show()
else:
    print("The required columns 'Symbol' and '%chng in OI' are not present in the dataset.")