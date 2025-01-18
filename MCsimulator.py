import pandas
import numpy
import matplotlib.pyplot as plt
import math as m
import random
import seaborn

# 1 - path simulation of underlying

def format_number(num):
    return f"{num:,.3f}"

# time must be greater than iter, should be fixed
mu = 0.05
sig = 0.2
iter = 300
time = 30
dt = time/iter
S0 = 100
paths = 10000
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
print(prices)
seaborn.distplot(prices)
plt.show()

# 2 - trade simulator based on underlying paths 
