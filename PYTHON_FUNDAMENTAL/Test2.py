import pandas as pd

# Sample DataFrame with Multi-Level Columns
data = {
    ('rating', 'size'): [10, 20],
    ('rating', 'mean'): [4.5, 4.8]
}
df = pd.DataFrame(data)
print(f"df data: {df}")
# Flatten column names
df.columns = [f'{i}|{j}' if j != '' else f'{i}' for i, j in df.columns]

print(f"\ndf2 data: {df}")