'''
# Variance measures how "spread-out" the data is.
Variance(q2) is simply the average of the squared differences from the mean
Example: What is the variance of the data set(1,4,5,4,8) ?
  (a) First find the mean : Mean = Sum of Numbers/Count = (1+4+5+4+8)/5 = 4.4
      Mean : 4.4
  (b) Now find the differences from the mean : data set - mean = 1-4.4 = -3.4
                                              Standard Deviations (-3.4, -0.4, 0.6,-0.4, 3.6)
  (c) Find the squared differences: (differences from the mean)sq = (-3.4)sq = 11.56
                                              Squared Variance (11.56, 0.16, 0.36, 0.16, 12.96)
  (d) Find the average of the squared variance differences:
      Average of Squared Variance = Variance(q2) = Sum of "squared differences"/Count = (11.56 + 0.16 + 0.36 + 0.16 + 12.96)/ 5 = 5.04
      Variance: 5.04
      Deviation: 2.244994432 # Square root of Variance

 # Sample variance:
       (S)sq =  Sum of "squared differences"/Count -1 =   (11.56 + 0.16 + 0.36 + 0.16 + 12.96)/ 4 = 6.3
'''
import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 50.0, 10000)
print(incomes)

print(f" Standard Variance :{incomes.var()}")
print(f" Standard Deviation :{incomes.std()}")

plt.hist(incomes,50)
plt.show()