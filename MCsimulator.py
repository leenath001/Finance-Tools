import pandas
import numpy
import matplotlib.pyplot as plt
import math as m
import random
import seaborn

# number formatting
def format_number(num):
    return f"{num:,.3f}" 
def format_bank(num):
    return f"{num:,.2f}" 


# 1 - PATH SIMULATION OF UNDERLYING (NORMAL SHOCKS, LOGN PRICES)

## goals - use statistics to estimate mu, sigma based on time, dt (expected mu/sigma through each dt) 

# data input (arr -> Motley Fool, vol -> Market Chameleon) IN PROGRESS
arr = .1476
vol = .134
tradingdays = 21
##

# estimation parameters
iter = 5000
time = 7
S0 = 100
paths = 50000
mu = .05
sig = .12
dt = time/iter
array = numpy.ones((paths, iter))
array2 = numpy.ones((paths, iter))

# iterates through array and changes each entry (by iteration then path)

for rowind, row in enumerate(array):
    for colind, entry in enumerate(row[1:iter+1]):
        entry = 1 + (mu * dt + sig * m.sqrt(dt) * numpy.random.randn())
        array[rowind,colind+1] = format_number(entry)
        entry = array[rowind,colind+1]
        entry *= array2[rowind,colind]
        array2[rowind,colind+1] = entry

# prices from last iteration of each path, along with random sampling of shocks
prices = S0 * array2[:,iter-1] 
randint = random.randint(0,iter)
shocks = array[:,randint]

# price range
min = min(prices)
max = max(prices)
print('Minimum of', f"{min:.2f}",', Maximum of', f"{max:.2f}")


# 2 - TRADE SIMULATOR BASED OFF UNDERLYING SIMULATION

#   GUIDE: set type to __ based on trade analysis wanted
#   1 - P[underlying >= strike]
#   2 - P[underlying <= strike]
#   3 - P[strike <= underlying <= strike2]
#   4 - P[strike >= underlying or underlying >= strike2]
#   SET COUNT & SUM TO 0, strike2 > strike!!

type = 4
strike = 75
strike2 = 150
count = 0
sum = 0

if type == 1:
    for p in prices:
        if p >= strike:
            count += 1
            sum += p
elif type == 2:
    for p in prices:
        if p <= strike:
            count += 1
            sum += p
elif type == 3:
    for p in prices:
        if p >= strike and p <= strike2:
            count += 1
            sum += p
elif type == 4:
    for p in prices:
        if p <= strike or p >= strike2:
            count += 1
            sum += p

prob = count/paths
ev = (1/paths) * sum
print(f"{prob:.2%}", "trade is ITM. Expected value of", f"{ev:.2f}")

'''
# normality check
plt.figure()
#plt.hist(shocks, bins = 40, density = True)
seaborn.distplot(shocks)
plt.xlabel('Shocks')
plt.ylabel('Count')
plt.title('Norm Dist of Shocks')
plt.show()
'''

# log-normality check
plt.figure()
plt.hist(prices,bins = 60, density = True)
#seaborn.distplot(prices)
plt.xlim(0,max)
plt.xlabel('Price')
plt.ylabel('Density')
plt.title('Log-Norm Dist of Prices')
if type == 3 or type == 4:
    plt.axvline(x = strike, color = 'red')
    plt.axvline(x = strike2, color = 'red')
else:
    plt.axvline(x = strike, color = 'red')
plt.show()
