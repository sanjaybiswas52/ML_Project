import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
print(f"Columns :{df.columns}")
print(f"Columns :{df['# Gears']}")
print(f"Group by Gears :\n{df[['# Gears','CombMPG']]}")
print(f"Gears   Count:{df['# Gears'].value_counts()}")
'''
gear_counts = df['# Gears'].value_counts()

# Define a unique color for each gear
unique_gears = gear_counts.index
bar_colors = plt.cm.tab10(range(len(unique_gears)))

gear_counts.plot(kind='bar', color=bar_colors)  # --------Bar Chart
plt.show()

#Histogram Chart
sns.distplot(df['CombMPG'])  # ---------------------------Distplot (Histogram)
plt.show()

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]
df2.head()
print(df2)
sns.scatterplot(x="Eng Displ", y="CombMPG", data=df) # --- Scatterplot
#sns.pairplot(df2, height=2.5);  #Seaborn currently has a bug with the hue parameter so we've omitted it
plt.show()

sns.pairplot(df2, hue='Cylinders', height=2.5) # --------- Pairplot Chart
plt.show()

#jointplot = Scatter Plot and Histogram
sns.jointplot(x="Eng Displ", y="CombMPG", data=df) # ----- Jointplot Chart
plt.show()
'''
#The "lmplot" is a scatterplot, but with a linear regression line computed and overlaid onto the data.
print(f"Group by Gears :\n{df[['Eng Displ','CombMPG']]}")
sns.lmplot(x="Eng Displ", y="CombMPG", data=df)  # ------- lmplot chart
plt.show()

ax=sns.swarmplot(x='Mfr Name', y='CombMPG', data=df) # --- swarmplot Chart
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.show()

sns.set(rc={'figure.figsize':(15,5)})
ax=sns.boxplot(x='Mfr Name', y='CombMPG', data=df) # ----- Boxplot
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.show()

ax=sns.swarmplot(x='Mfr Name', y='CombMPG', data=df)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.show()

ax=sns.countplot(x='Mfr Name', data=df)
ax.set_xticklabels(ax.get_xticklabels(),rotation=45)
plt.show()

df2 = df.pivot_table(index='Cylinders', columns='Eng Displ', values='CombMPG', aggfunc='mean')
sns.heatmap(df2)
plt.show()