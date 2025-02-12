import matplotlib.pyplot as plt
plt.rcdefaults()

values = [12,55,4,42,14]
labels = ['India','United States','Russia','China','Europe']


#Pie Chart
#colors = ['r','g','b','c','m']
colors = ['red', 'blue', 'green', 'orange', 'purple']
explode = [0,0,0.2,0,0]

#plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.figure(figsize=(6, 6))
plt.pie(values, colors=colors, labels=labels, explode=explode, autopct='%1.1f%%')
plt.title('Student Locations')
#plt.show()

#Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(labels, values, color = colors)
#plt.show()

#Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(values, labels, alpha=0.7, s=200, c=colors, edgecolors='black')
plt.yticks(labels, labels)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()