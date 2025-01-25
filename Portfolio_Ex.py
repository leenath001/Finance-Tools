import MC_funcs
import matplotlib.pyplot as plt
import seaborn
import numpy

# number formatting
def form_p(num):
    return f"{num:.2%}"
def form_b(num):
    return f"{num:.2f}"

# make a loop that takes names and allocations 
# parameters and asset allocation
iter = 1000
days = 25
paths = 1000
COSTalo = 50
METAalo = 25
GOOGalo = 25
NVDAalo = 25
GSalo = 75
initsum = 200

# turning on price level analysis (0 : off, 1 : > strike, 2 < strike)
type = 1
strike = 215

# running simulations and loading data
COST = MC_funcs.asset_sim(iter,days,COSTalo,paths,"Data/COST.xlsx")
META = MC_funcs.asset_sim(iter,days,METAalo,paths,"Data/META.xlsx")
GOOG = MC_funcs.asset_sim(iter,days,GOOGalo,paths,"Data/GOOG.xlsx")
NVDA = MC_funcs.asset_sim(iter,days,NVDAalo,paths,"Data/NVDA.xlsx")
GS = MC_funcs.asset_sim(iter,days,GSalo,paths,"Data/GS.xlsx")

# calling parameters [drift, volatility]
COSTp = [form_p(COST[1]),form_p(COST[2])]
METAp = [form_p(META[1]),form_p(META[2])]
GOOGp = [form_p(GOOG[1]),form_p(GOOG[2])]
NVDAp = [form_p(NVDA[1]),form_p(NVDA[2])]
GSp = [form_p(GS[1]),form_p(GS[2])]

print('COST params = ', COSTp) 
print('META params = ', METAp)
print('GOOG params = ', GOOGp)   
print('TSLA params = ', NVDAp)   
print('GS params = ', GSp)   
print()

# analysis and charts
port = COST[0] + META[0] + GOOG[0] + NVDA[0] + GS[0]
min = form_b(min(port))
max = form_b(max(port))
mean = sum(port)/paths
pgrowth = form_p(abs(initsum - mean)/mean)

print('Minimum of', min, ', Maximum of', max)
print('Initial Value: $',initsum)
print('Average Value: $',form_b(mean))
print('Growth: ',pgrowth)
print()

# P[portfolio > or < strike]
MC_funcs.prob_tool(1,215,port,paths)

plt.figure()
plt.hist(port,bins = 60, density = True)
seaborn.kdeplot(port)
plt.axvline(x = initsum, c = 'lime')
plt.xlabel('Price')
plt.ylabel('Density')
plt.axvline(x = strike, color = 'red')
plt.title('Price Distribution')
plt.show()


