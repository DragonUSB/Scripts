import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from colorama import init, Back

plt.style.use('seaborn-darkgrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

datos = pd.read_csv('ETHUSDT_1d.csv', sep = ",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

# Media Movil Simple
def MA(df, n):
    MA = pd.Series(pd.Series.rolling(df['Close'], n).mean(), name = 'MA_' + str(n))
    df = df.join(MA)
    return df

# Media Movil Exponencial
def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'], span = n, min_periods = n - 1, adjust = False).mean(), name = 'EMA_' + str(n))
    df = df.join(EMA)
    return df

#Pi Cycle Top
datos = MA(datos, 111)
datos = MA(datos, 350)
datos['MA_350_2'] = 2 * datos['MA_350']

#Pi Cycle Bottom
datos = MA(datos, 471)
datos['MA_471_0745'] = 0.745 * datos['MA_471']
datos = EMA(datos, 150)

# Grafico con matplotlib
fig = plt.figure(figsize = (12, 6))
fig.suptitle('Pi Cycle Top')
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos['MA_111'])
plt.plot(datos.index, datos['MA_350_2'])
plt.grid(True)
plt.show()

fig = plt.figure(figsize = (12, 6))
fig.suptitle('Pi Cycle Bottom')
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos['MA_471_0745'])
plt.plot(datos.index, datos['EMA_150'])
plt.grid(True)
plt.show()