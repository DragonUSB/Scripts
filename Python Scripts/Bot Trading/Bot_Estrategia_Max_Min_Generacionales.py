import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from colorama import init, Back

plt.style.use('seaborn-v0_8-whitegrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

datos = pd.read_csv('Scripts/Python Scripts/BTCUSDT_1d.csv', sep = ",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

def sma(df, d):
    c = df.rolling(d).mean()
    return c.dropna()

datos['mv730'] = sma(datos.Close, 730)
datos['mv730x5'] = datos['mv730'] * 5

df_test = datos.copy()
# df_test = datos.iloc[-int(len(datos) / 2):,:].copy()

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(df_test.index, df_test.Close)
plt.plot(df_test.index, df_test.mv730)
plt.plot(df_test.index, df_test.mv730x5)
plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()