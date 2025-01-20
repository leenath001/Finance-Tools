1 - PATH SIMULATION OF UNDERLYING

Takes parameters drift, volatility, time, starting price, and no. of paths to simulate stock movement with Geometric Brownian Motion (GBM) assumption

*  mu : drift (annualized)
*  sig : volatility (annualized)
*  iter : number of GBM iterations - this parameter discretizes time
*  days : length of simulation (code annualizes time automatically)
*  S0 : starting stock price
*  paths : no. of simultaneous simulations wanted

array gives a [paths x iter] matrix of shocks. For entry (path_i, iter_j), we get a specific shock for the specified period.

array2 gives a [paths x iter] matrix of returns as of period iteration_i. For entry (path_i, iter_j), shocks are multiplied across such that our entry is a % return as of specified period.

Use plots to verify normality of shocks & log-normality of return

2 - TRADE SIMULATOR BASED OFF UNDERLYING

Using data from (1), code analyzes all outcomes to provide P[profit].

GUIDE: set type to __ based on trade analysis wanted
*  1 - P[underlying >= strike]
*  2 - P[underlying <= strike]
*  3 - P[strike <= underlying <= strike2]
*  4 - P[strike >= underlying or underlying >= strike2]
SET COUNT & SUM TO 0, strike2 > strike!!

Features to be added: 
*  use stats/historical data to estimate drift and vol (annualized)
*  EV calculator (in progress)
