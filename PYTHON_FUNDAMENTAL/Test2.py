#import pandas as pd

def divisible_3(num):
    #return num % 3 == 0
    val = num % 3
    if val == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is not divisible by 3")


print(divisible_3(21))