import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_parquet('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/Parquet_file/cars.parquet')
X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].values)

# Add a constant column to our model so we can have a Y-intercept
X = sm.add_constant(X)

print (X)

est = sm.OLS(y, X).fit()

print(est.summary())

print(f"Probability based on Door\n{y.groupby(df.Doors).mean()})")


