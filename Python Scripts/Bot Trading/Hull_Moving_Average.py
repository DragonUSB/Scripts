from cv2 import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_4h.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)

# Weighted Moving Average
def WMA(df, n):
    weights = np.arange(1, n + 1)
    WMA = pd.Series(pd.Series.rolling(df['Close'], n).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw = True), name = 'WMA_' + str(n))
    df = df.join(WMA)
    return df

wma_50 = WMA(datos, 50)
wma_200 = WMA(wma_50, 200)

df = wma_200[['Close', 'WMA_50', 'WMA_200']]
df.plot(figsize = (12,6))

# Hull Moving Average
def HMA(df, n):
    df1 = pd.DataFrame({'Close': []})
    WMA1 = WMA(df, n)
    WMA1str = 'WMA_' + str(n)
    WMA2 = WMA(WMA1, n // 2)
    WMA2str = 'WMA_' + str(n // 2)
    sqrtn = pow(n, 0.5)
    df1['Close'] = 2 * WMA2[WMA2str] - WMA2[WMA1str]
    HMA = WMA(df1, int(sqrtn))
    HMA2str = 'WMA_' + str(int(sqrtn))
    HMA = pd.Series(HMA[HMA2str], name = 'HMA_' + str(n))
    df = df.join(HMA)
    return df

df1 = HMA(datos, 55)
df2 = WMA(df1, 55)
df3 = df2[['Close', 'WMA_55', 'HMA_55']].copy()
df3.plot(figsize = (12, 6))

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df2['WMA_55'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df2['HMA_55'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(df2, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df4 = df2.iloc[-90:-1,:]
ap1 = [ mpf.make_addplot(df4['WMA_55'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df4['HMA_55'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(df4, type = 'candle', volume = True, style = 'binance', addplot = ap1)

df3['MHULL'] = df3['HMA_55'].shift(0)
df3['SHULL'] = df3['HMA_55'].shift(2)

# Plot
fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(df3.index, df3.Close)
# plt.plot(df3.index, df3.MHULL, label = 'MHULL', color = 'green')
# plt.plot(df3.index, df3.SHULL, label = 'SHULL', color = 'red')
plt.fill_between(df3.index, df3.MHULL, df3.SHULL, where=df3.MHULL >= df3.SHULL, color='green')
plt.fill_between(df3.index, df3.MHULL, df3.SHULL, where=df3.MHULL < df3.SHULL, color='red')
plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()