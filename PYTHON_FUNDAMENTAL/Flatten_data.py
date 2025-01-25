import pandas as pd

# Sample DataFrame with Multi-Level Columns
data = {
    ('rating', 'size'): [10, 20],
    ('rating', 'mean'): [4.5, 4.8]
}
df = pd.DataFrame(data)
print(f"Original DataFrame:\n{df}")

# Flatten column names
#df.columns = [f'{i}|{j}' if j != '' else f'{i}' for i, j in df.columns]
#     OR
# Flatten column names (more explicit)
new_columns = []
for i, j in df.columns:
    if j:  # Check if the second part of the column name is not empty
        new_columns.append(f'{i}|{j}')
    else:
        new_columns.append(f'{i}')

df.columns = new_columns
print(f"\nFlattened DataFrame:\n{df}")
