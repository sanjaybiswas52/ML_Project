import pandas as pd

data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [5000, 7000, 6000, 8000, 6500, 7500]
}

df = pd.DataFrame(data)

# Group by 'Department' and calculate the sum of 'Salary'
grouped = df.groupby('Department')['Salary'].sum()
print(grouped)