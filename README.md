Takes parameters drift, volatility, time, starting price, and no. of paths to simulate stock movement with Geometric Brownian Motion (GBM) assumption

mu : drift
sig : volatility
iter : number of GBM iterations - this parameter discretizes time
time : length of simulation
S0 : starting stock price
paths : no. of MC simulations wanted

array gives a [paths x iter] matrix of shocks. For entry (path_i, iter_j), we get a specific shock for the specified period.
array2 gives a [paths x iter] matrix of returns as of period iteration_i. For entry (path_i, iter_j), shocks are multiplied across such that our entry is a % return as of specified period.

Use plots to verify normality of shocks & log-normality of return

Features to be added: 
use statistics to estimate mu, sigma based on time, dt (expected mu/sigma through each dt) 

