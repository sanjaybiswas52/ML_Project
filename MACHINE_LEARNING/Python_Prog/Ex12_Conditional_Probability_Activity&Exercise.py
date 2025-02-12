from numpy import random
import pyarrow
import subprocess

# Execute a terminal command for clear screen
cls = subprocess.run(["clear"], capture_output=True, text=True)
print(cls.stdout)

# Set the random seed for reproducibility
random.seed(0)

# Initialize dictionaries to track totals and purchases
totals    = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
purchases = {20: 0, 30: 0, 40: 0, 50: 0, 60: 0, 70: 0}
totalPurchases = 0
print(f"totals Before Loop   : {totals} \npurchase Before Loop : {purchases}")

# Simulate the random selection process
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade) / 100.0

    # Increment the totals for the selected age decade
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

print(f"\ntotals Post Loop   : {totals} \npurchase Post Loop : {purchases} \n\ntotal Purchase : {totalPurchases}\n ")

'''
Let's play with conditional probability.

First let's compute P(E|F), where E is "purchase" and F is "you're in your 30's". 
The probability of someone in their 30's buying something is just the percentage of how many 30-year-olds bought something:
E is "purchase" [30: 4974]
F is 30-year-olds
'''
PEF = float(purchases[30]) / float(totals[30])
print(f"PEF = 30-year-olds bought P(E|F)(purchase(30's) out of [30: 4974]/[30: 16619]) \
 \n    = {float(purchases[30])}/{float(totals[30])} = {str(PEF)}\n")

#P(F) is just the probability of being 30 in this data set:
PF = float(totals[30]) / 100000.0
print("PF = Being 30 in this data set PF(30's) 16619  out of 100000                  : " +  str(PF))

#And P(E) is the overall probability of buying something, regardless of your age:
PE = float(totalPurchases) / 100000.0
print("PE = Overall probability of buying something P(Purchase)=45012 out of 100000  : " + str(PE) +"\n")

'''
If E and F were independent, then we would expect P(E | F) to be about the same as P(E). 
But they're not; P(E) is 0.45, and P(E|F) is 0.3. So, that tells us that E and F are dependent 
(which we know they are in this example.)

P(E,F) is different from P(E|F). 
P(E,F) would be the probability of both being in your 30's 
and buying something, out of the total population - not just the population of people in their 30's:
P(E,F) = P(E)P(F).
P(E|F) = P(E,F)/P(F)
'''
print("P(30's, Purchase)                    :" + str(float(purchases[30]) / 100000.0))
#Let's also compute the product of P(E) and P(F), P(E)P(F):
print("P(30's)P(Purchase) P(E,F) = P(E)P(F) :" + str(PE * PF))
print("P(E|F) = P(E,F)/P(F)                 :" + str(float(purchases[30] / 100000.0) / PF))