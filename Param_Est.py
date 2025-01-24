def Param_Est(sheet):

    import pandas as pd
    import numpy as np

# data import/indexing
    data = pd.read_excel(sheet)
    cols = ['dS/S','ln(H/L)']
    paramestdat = data[cols]

# parameter estimation
    dS_S = paramestdat['dS/S']
    ln_HL = paramestdat['ln(H/L)']

    mu = sum(dS_S)
    vol = np.sqrt(252)*np.sqrt((sum(ln_HL))/(1008*np.log(2)))

    return mu, vol