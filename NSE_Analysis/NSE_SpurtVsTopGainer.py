import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def load_csv(file_path):
    """
    Load a CSV file and handle potential errors.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded: {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: The file '{file_path}' is not in a valid CSV format.")
        return None

# Calculate dates for file paths
p_spurt = datetime.today() - timedelta(days=0)
p_gainerlooser = datetime.today() - timedelta(days=0)
spurt_date = p_spurt.strftime('%d%m%Y')
topg_date = p_gainerlooser.strftime('%d-%b-%Y')
file1_path = f"/Users/sanjaybiswas/Downloads/Spurts-in-OI-By-Underlying-{spurt_date}.csv"
file2_path_losers = f"/Users/sanjaybiswas/Downloads/T20-GL-loosers-NIFTY-{topg_date}.csv"
file2_path_gainers = f"/Users/sanjaybiswas/Downloads/T20-GL-gainers-NIFTY-{topg_date}.csv"

# Load datasets
spurt_data1 = load_csv(file1_path)
data2_losers = load_csv(file2_path_losers)
data2_gainers = load_csv(file2_path_gainers)

# Ensure necessary columns exist
if spurt_data1 is not None and 'Symbol' in spurt_data1.columns and '%chng in OI' in spurt_data1.columns:
    # Exclude rows where the symbol contains "NIFTY" and filter `%chng in OI > 50.0`
    spurt_data1['Symbol'] = spurt_data1['Symbol'].str.strip()  # Strip whitespace
    spurt_data = spurt_data1[
        (~spurt_data1['Symbol'].str.contains('NIFTY', case=False, na=False)) &
        (spurt_data1['%chng in OI'] > 4.0)
    ]

    # Sort data by `%chng` for top 10 gainers and losers
    losers_data = data2_losers[data2_losers['%chng'] <= -1.2]
    gainers_data = data2_gainers[data2_gainers['%chng'] >= 1.2]

    top10_losers = losers_data.nsmallest(15, '%chng').sort_values(by='%chng', ascending=False)
    top10_gainers = gainers_data.nlargest(15, '%chng').sort_values(by='%chng', ascending=False)

    # Combine top 10 gainers and losers
    gainer_looser_data = pd.concat([top10_gainers, top10_losers], ignore_index=True)

    # Strip whitespace in `Symbol` for both datasets to ensure matching works
    gainer_looser_data['Symbol'] = gainer_looser_data['Symbol'].str.strip()

    # Perform a left join of `gainer_looser_data` with `spurt_data` on the "Symbol" column
    try:
        merged_data = pd.merge(
            gainer_looser_data,
            spurt_data,
            on="Symbol",
            how="inner",
            suffixes=("_combined", "_filtered")
        )
        print("Merge successful.")
    except Exception as e:
        print(f"Error during merge: {e}")
        merged_data = pd.DataFrame()  # Fallback in case of error

    # Save the merged symbols to a file
    out_file = f"/Users/sanjaybiswas/Downloads/topgainer_Looser_stocks_{spurt_date}.txt"
    merged_data[['Symbol']].to_csv(out_file, index=False, header=False)
    print(f"Merged data saved to file. {merged_data[['Symbol']]}")

    # Create the bar chart
    plt.figure(figsize=(12, 8))

    # Define colors and bar width
    bar_width = 0.4
    symbols_combined = merged_data['Symbol']
    values_combined = merged_data['%chng']

    # Plot the chart
    bar_positions = range(len(symbols_combined))
    plt.bar(
        bar_positions,
        values_combined,
        color=['green' if v > 0 else 'red' for v in values_combined],
        alpha=0.7
    )

    # Add titles and labels
    plt.title('Top 10 Gainers and Losers by % Change', fontsize=14)
    plt.xlabel('Symbol', fontsize=12)
    plt.ylabel('% Change', fontsize=12)
    plt.xticks(bar_positions, symbols_combined, rotation=45, ha='right', fontsize=10)
    plt.tight_layout()

    # Show the plot
    plt.show()
else:
    print("The required columns are not present in the dataset.")