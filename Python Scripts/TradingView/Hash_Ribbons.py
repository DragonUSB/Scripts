import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
from itertools import compress
from typing import Sequence

quandl.ApiConfig.api_key = "MGz7SvL7fiWyqe_j8QKM"
datos1 = quandl.get("BCHAIN/HRATE")
datos2 = pd.read_csv('C:/Users/Fernando Conquet/Documents/Python Scripts/Bot Trading/BTCUSDT_1d.csv', sep = ",")
datos2['Open_Timestamp'] = pd.to_datetime(datos2['Open_Timestamp'], format='%Y-%m-%d')
datos2 = datos2[['Open_Timestamp', 'Close']].copy()
datos2 = datos2.rename(columns={'Open_Timestamp': 'Date'})
datos2.set_index('Date', inplace = True)
datos1['Close'] = pd.Series([], dtype = 'float64')
for i in range(len(datos1)):
    for j in range(len(datos2)):
        if datos1.index[i] == datos2.index[j]:
            datos1.Close[i] = datos2.Close[j]

# Media Movil Simple
def MA(df, n, name):
    if name == 'HR_Short' or name == 'HR_Long':
        MA = pd.Series(pd.Series.rolling(df['Value'], n).mean(), name = name)
    else:
        MA = pd.Series(pd.Series.rolling(df['Close'], n).mean(), name = name)
    df = df.join(MA)
    return df

def barssince(condition, default = 0):
    barssince = []
    for i in range(len(condition)):
        numero = next(compress(range(len(condition[:i + 1])), reversed(condition[:i + 1])), default)
        barssince.append(numero)
    barssince = pd.Series(barssince, index = datos1.index, name = 'barssince')
    return barssince

def crossover(series1, series2):
    crossover = (series1 < series2) & (series1.shift(-1) > series2.shift(-1))
    return crossover

def crossunder(series1, series2):
    crossunder = (series1 > series2) & (series1.shift(-1) < series2.shift(-1))
    return crossunder

# HASH RATE MA
datos1 = MA(datos1, 30, 'HR_Short')
datos1 = MA(datos1, 60, 'HR_Long')
datos1 = MA(datos1, 10, 'S10')
datos1 = MA(datos1, 20, 'S20')

# INDICATORS
HR_Short = datos1['HR_Short']
HR_Long = datos1['HR_Long']

S10 = datos1['S10']
S20 = datos1['S20']

Capitulation = crossunder(HR_Short, HR_Long)
datos1['Capitulation'] = Capitulation
datos1['Capitulation'] = datos1.apply(lambda x: ((x.HR_Long + x.HR_Short) / 2) if x.Capitulation == True else np.nan, axis = 1)
Miner_Capitulation = HR_Short < HR_Long
datos1['Miner_Capitulation'] = Miner_Capitulation
datos1['Miner_Capitulation'] = datos1.apply(lambda x: ((x.HR_Long + x.HR_Short) / 2) if x.Miner_Capitulation == True else np.nan, axis = 1)
Recovering = (HR_Short > HR_Short.shift(1)) & (HR_Short > HR_Short.shift(2)) & (HR_Short > HR_Short.shift(3)) & (HR_Short < HR_Long)
datos1['Recovering'] = Recovering
datos1['Recovering'] = datos1.apply(lambda x: ((x.HR_Long + x.HR_Short) / 2) if x.Recovering == True else np.nan, axis = 1)
Recovered = crossover(HR_Short, HR_Long)
datos1['Recovered'] = Recovered
datos1['Recovered'] = datos1.apply(lambda x: ((x.HR_Long + x.HR_Short) / 2) if x.Recovered == True else np.nan, axis = 1)

# HASH BOTTOM + PA SIGNAL
Buy = (
     (crossover(S10, S20) & (barssince(Recovered) < barssince(crossunder(S10, S20))) & (barssince(Recovered) < barssince(Capitulation))) | 
     ((S10 > S20) & crossover(HR_Short, HR_Long))
     )
datos1['Buy'] = Buy
datos1['Buy'] = datos1.apply(lambda x: ((x.HR_Long + x.HR_Short) / 2) if x.Buy == True else np.nan, axis = 1)

# HALVINGS
halving_1 = datos1.index == '2012-11-28'
halving_2 = datos1.index == '2016-7-9'
halving_3 = datos1.index == '2020-5-12'

# PLOT
fig = plt.figure(figsize = (10, 4))
ax1 = plt.subplot()
plt.plot(datos1.index, datos1.HR_Long, color = 'gray')
plt.plot(datos1.index, datos1.HR_Short)
plt.fill_between(datos1.index, datos1.HR_Short, datos1.HR_Long, where = (datos1.HR_Short < datos1.HR_Long), color = 'red', alpha = 0.7, interpolate = True)
plt.scatter(x = datos1.index, y = datos1['Capitulation'], color = 'gray', marker = '.', s = 15**2, alpha = .5)
plt.scatter(x = datos1.index, y = datos1['Miner_Capitulation'], color = 'green', marker = '.', s = 15**2, alpha = .1)
plt.scatter(x = datos1.index, y = datos1['Recovered'], color = 'lime', marker = '.', s = 15**2, alpha = 1)
plt.scatter(x = datos1.index, y = datos1['Recovering'], color = 'green', marker = '.', s = 15**2, alpha = .5)
plt.scatter(x = datos1.index, y = datos1['Buy'], color = 'blue', marker = '.', s = 15**2, alpha = 1)
plt.axvline(datos1.index[halving_1], color='r',linewidth=5,alpha=0.8)
plt.axvline(datos1.index[halving_2], color='r',linewidth=5,alpha=0.8)
plt.axvline(datos1.index[halving_3], color='r',linewidth=5,alpha=0.8)
plt.grid(True)
plt.title('Hash Ribbons')
plt.show()