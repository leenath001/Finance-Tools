import pandas
import numpy
import matplotlib.pyplot as plt
import math as m
import random
import seaborn

# 1 - PATH SIMULATION OF UNDERLYING (NORMAL SHOCKS, LOGN PRICES)

def format_number(num):
    return f"{num:,.3f}" 
def format_bank(num):
    return f"{num:,.2f}" 

# params
mu = 0.05
sig = 0.1
iter = 300
time = 30
dt = time/iter
S0 = 100
paths = 50000
array = numpy.ones((paths, iter))
array2 = numpy.ones((paths, iter))

# flexible code iterates through array and changes each entry 
# array is matrix of random shocks that occur each period
# array2 provides return as of certain period 
    
for rowind, row in enumerate(array):
    for colind, entry in enumerate(row[1:iter+1]):
        entry = 1 + (mu * dt + sig * m.sqrt(dt) * numpy.random.randn())
        array[rowind,colind+1] = format_number(entry)
        entry = array[rowind,colind+1]
        entry *= array2[rowind,colind]
        array2[rowind,colind+1] = entry

prices = S0 * array2[:,iter-1] 
randint = random.randint(0,iter)
shocks = array[:,randint]

print(min(prices))
print(max(prices))

plt.figure(1)
seaborn.distplot(shocks)
plt.xlabel('Shocks')
plt.ylabel('Count')
plt.title('Norm Dist of Shocks')
plt.show()

plt.figure(2)
plt.hist(prices,bins= 60, density = True)
#seaborn.distplot(prices)
plt.xlim(0,max(prices))
plt.xlabel('Price')
plt.ylabel('Density')
plt.title('Log-Norm Dist of Prices')
plt.show()

# 2 - TRADE SIMULATOR BASED OFF UNDERLYING SIMULATION
