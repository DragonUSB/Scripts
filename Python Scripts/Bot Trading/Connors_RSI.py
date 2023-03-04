import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

datos = pd.read_csv('ETHUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume', 'Ignore']].copy()
datos.set_index('Close_Timestamp', inplace = True)
datos = datos.iloc[-1000:,:]

UpDown = 0
list = [0]
for i in range(1, len(datos)):
    d0, d1 = datos.Close[i], datos.Close[i-1]
    if d0 > d1:
        UpDown = max(1, UpDown + 1)
    elif d0 < d1:
        UpDown = min(-1, UpDown - 1)
    else:
        UpDown = 0
    list.append(UpDown)
list = pd.Series(list, index = datos.index, name = 'UpDown')
datos = datos.join(list)

# Rate of Change (ROC)
def ROC(df, n):
    M = df['Close'].diff(n - 1)
    N = df['Close'].shift(n - 1)
    ROC = pd.Series((M / N) * 100, name = 'ROC_' + str(n))
    df = df.join(ROC)
    return df

# RSI
def RSI(df, c, n):
    df['diff'] = df[c].diff(periods = 1)
    # df.dropna(inplace = True)
    df['sub'] = df['diff'][df['diff'] > 0]
    df['baj'] = abs(df['diff'][df['diff'] <= 0])
    df.fillna(value = 0, inplace = True)
    media_sub = df['sub'].rolling(window = n).mean()
    media_baj = df['baj'].rolling(window = n).mean()
    RSI = pd.Series(100 - (100 / (1 + (media_sub / media_baj))), name = 'RSI_' + str(n))
    df = df.join(RSI)
    df.drop(columns = ['diff','sub','baj'], inplace = True)
    return df

#  Percent Rank
def PercentRank(df, n):
    pctrank = lambda x: pd.Series(x).rank(pct = False).iloc[-1]
    percentrank = df['ROC_2'].rolling(window = n, center = False).apply(pctrank, raw = True)
    PercentRank = pd.Series(percentrank, name = 'PercentRank')
    df = df.join(PercentRank)
    return df

datos = RSI(datos, 'Close', 3)
datos = RSI(datos, 'UpDown', 2)
datos = ROC(datos, 2)
datos = PercentRank(datos, 100)

# Connors RSI
def CRSI(df):
    CRSI = pd.Series((df['RSI_3'] + df['RSI_2'] + df['PercentRank']) / 3, name = 'CRSI')
    df = df.join(CRSI)
    return df

df2 = CRSI(datos)
Nivel_30 = pd.Series(df2['Ignore'] + 30, name = 'Nivel_30')
Nivel_70 = pd.Series(df2['Ignore'] + 70, name = 'Nivel_70')
df2 = df2.join(Nivel_30)
df2 = df2.join(Nivel_70)

fig = plt.figure(figsize = (12,6))
plt.subplot(2, 1, 1)
plt.plot(df2.Close)
plt.title('Precio del UNI')
plt.subplot(2, 1, 2)
plt.plot(df2.CRSI)
plt.plot(df2.Nivel_30, color = 'r')
plt.plot(df2.Nivel_70, color = 'r')
plt.show()

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df2['CRSI'], color = 'b', panel = 2),
        mpf.make_addplot(df2['Nivel_30'], color = 'r', panel = 2),
        mpf.make_addplot(df2['Nivel_70'], color = 'r', panel = 2)
      ]
mpf.plot(df2, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df3 = df2.iloc[-100:,:]
ap1 = [ mpf.make_addplot(df3['CRSI'], color = 'b', panel = 2),
        mpf.make_addplot(df3['Nivel_30'], color = 'r', panel = 2),
        mpf.make_addplot(df3['Nivel_70'], color = 'r', panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap1)