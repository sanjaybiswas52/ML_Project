import matplotlib.pyplot as plt
import numpy as np
from pylab import *

'''
List a = [1,2,3]
List b = [40,50,60]

Function def de_mean(x):
   Mean = 2
       [1-2, 2-2, 3-3]
 -----------------------------
    a :[-1.0, 0.0, 1.0]
 -----------------------------
Similarly for b
 _____________________________
     b :[-10.0, 0.0, 10.0]
 -----------------------------
 function dot(de_mean(x), de_mean(y)) 
     =(-1.0 * -10.0) + (0.0 * 0.0) + (1.0 * 10.0)
     = 10.0 + 0.0 + 10.0
     = 20
     
Function def covariance(x, y):
   n = len(a) = 3
   n-1 = 2
   covariance = dot(de_mean(x), de_mean(y)) / (n-1)
              = 20 /2
              = 10
'''
def de_mean(x):
    xmean = np.mean(x)
    #return [xi - xmean for xi in x]
    return [float(xi - xmean) for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy  #In real life you'd check for divide by zero here
'''
a = [1,2,3,4,5,6,7,8,9]
b = [40,50,60,70,80,90,10,20,30]
'''
a = np.random.normal(3.0, 1.0, 1000)
b = np.random.normal(50.0, 10.0, 1000)

print(f"Value of a :{a}")
print(f"Value of b :{b}")
print(f"de_mean of a :{de_mean(a)}")
print(f"de_mean of b :{de_mean(b)}")
print(f"\n ----- covariance & correlation Func")

print(f"Func covariance : {covariance(a, b)}")
print(f"Func correlation : {correlation(a, b)}")
#print(f"Func Result : {scatter(a, b)}")
#plt.show()
