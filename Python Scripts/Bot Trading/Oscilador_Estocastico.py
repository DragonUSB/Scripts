import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

def STOK(df):
    STOK = pd.Series((df['Close'] - df['Low']) / (df['High'] - df['Low']), name = 'STOK')
    df = df.join(STOK)
    return df

df1 = STOK(datos)
df1 = df1[['Close', "STOK"]]

fig = plt.figure(figsize = (12,6))
ax1 = plt.subplot(211)
plt.plot(df1.Close)
plt.grid(True)
plt.title('Precio del UNI')    
ax1 = plt.subplot(212, sharex = ax1)
plt.plot(df1.STOK, color = 'r')
plt.grid(True)
plt.show()

def STOKexp(df, nK, nD, nS = 1):
    STOK = pd.Series((df['Close'] - df['Low'].rolling(nK).min()) / (df['High'].rolling(nK).max() - df['Low'].rolling(nK).min()), name = 'STOK' + str(nK))
    STOD = pd.Series(STOK.ewm(ignore_na = False, span = nD, min_periods = nD - 1, adjust = True).mean(), name = 'STOD' + str(nD))
    STOK = STOK.ewm(ignore_na = False, span = nS, min_periods = nS -1, adjust = True).mean()
    STOD = STOD.ewm(ignore_na = False, span = nS, min_periods = nS -1, adjust = True).mean()
    df = df.join(STOK)
    df = df.join(STOD)
    return df

df2 = STOKexp(datos, 14, 3)

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot(211)
plt.plot(df2.Close)
plt.grid(True)
plt.title('Precio del UNI')    
ax1 = plt.subplot(212, sharex = ax1)
plt.plot(df2.STOK14, color = 'r')
plt.plot(df2.STOD3, color = 'g')
plt.axhline(y = 0.8, color = 'k', linestyle = '--')
plt.axhline(y = 0.2, color = 'k', linestyle = '--')
plt.legend()
plt.show()

def STOKs(df, nK, nD, nS = 1):
    STOK = pd.Series((df['Close'] - df['Low'].rolling(nK).min()) / (df['High'].rolling(nK).max() - df['Low'].rolling(nK).min()), name = 'STOK' + str(nK))
    STOD = pd.Series(STOK.rolling(window = nD, center = False).mean(), name = 'STOD' + str(nD))
    STOK = STOK.rolling(window = nS, center = False).mean()
    STOD = STOD.rolling(window = nS, center = False).mean()
    df = df.join(STOK)
    df = df.join(STOD)
    return df

df3 = STOKs(datos, 14, 3)

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot(211)
plt.plot(df3.Close)
plt.grid(True)
plt.title('Precio del UNI')    
ax1 = plt.subplot(212, sharex = ax1)
plt.plot(df3.STOK14, color = 'r')
plt.plot(df3.STOD3, color = 'g')
plt.axhline(y = 0.8, color = 'k', linestyle = '--')
plt.axhline(y = 0.2, color = 'k', linestyle = '--')
plt.legend()
plt.show()

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df3['STOK14'], color = 'g', panel = 2),
        mpf.make_addplot(df3['STOD3'], color = 'b', panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df4 = df3.iloc[-30:-1,:]
ap1 = [ mpf.make_addplot(df4['STOK14'], color = 'g', panel = 2),
        mpf.make_addplot(df4['STOD3'], color = 'b', panel = 2)
      ]
mpf.plot(df4, type = 'candle', volume = True, style = 'binance', addplot = ap1)