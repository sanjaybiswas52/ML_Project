import pandas as pd
import subprocess

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

#1. Binning Data into Equal-Width Bins
data = [1, 7, 5, 4, 6, 12, 18, 25, 27]
binned = pd.cut(data, bins=3)

print(f"\nCut Data into Equal-Width Bins(3) : {binned}\n")

#2. Specifying Bin Edges
bin_edges = [0, 10, 20, 30]
binned = pd.cut(data, bins=bin_edges)

print(f"\nCut Data into ESpecifying Bin Edges : {binned}\n")

binned, bin_edges = pd.cut(data, bins=bin_edges, retbins=True)
print(f"\nBins : {binned}\nbin_edges :{bin_edges}\n")

#3. Adding Custom Labels
binned = pd.cut(data, bins=4, labels=["Low", "Medium", "High", "Very High"])

print(f"\nCut Data Custom Labels: {binned}\n")