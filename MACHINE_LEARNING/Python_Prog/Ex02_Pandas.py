import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/sanjaybiswas/Documents/Pycharm/MLCourse/PastHires.csv")
print(df)
print(f" shape : {df.shape}")
print(f" size : {df.size}")
print(f" len : {len(df)}")
print(f" Columns : {df.columns}")
print(f" Column Values :\n{df['Years Experience']}")
print(f" Row 0to4 Values :\n{df['Years Experience'][:5]}")
print(f" Row # 5  :\n{df['Years Experience'][4]}")
print(f" Columns  :\n{df[['Years Experience', 'Level of Education']]}")
print(f" Short values \n {df.sort_values('Years Experience')}")
sort_df = df.sort_values('Years Experience')
print(f" Columns  :\n{sort_df[['Years Experience', 'Level of Education']]}")

degree_counts = df['Level of Education'].value_counts()
print(f"count \n {degree_counts}")
#print(f"count \n {df[['Years Experience', 'Level of Education']].value_counts()}")
degree_counts.plot(kind='bar').show()

