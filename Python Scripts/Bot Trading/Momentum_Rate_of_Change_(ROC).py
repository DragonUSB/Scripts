import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

# Momentum
def MOM(df, n):
    M = pd.Series(df['Close'].diff(n), name = 'Momentum_' + str(n))
    df = df.join(M)
    return df

df1 = MOM(datos, 50)

fig = plt.figure(figsize = (12,6))
plt.subplot(2, 1, 1)
plt.plot(df1.Close)
plt.title('Precio del UNI')
plt.subplot(2, 1, 2)
plt.plot(df1.Momentum_50)
plt.show()

# Rate of Change (ROC)
def ROC(df, n):
    M = df['Close'].diff(n - 1)
    N = df['Close'].shift(n - 1)
    ROC = pd.Series(M / N, name = 'ROC_' + str(n))
    df = df.join(ROC)
    return df

df2 = ROC(df1, 50)

fig = plt.figure(figsize = (12,6))
plt.subplot(2, 1, 1)
plt.plot(df2.Close)
plt.title('Precio del UNI')
plt.subplot(2, 1, 2)
plt.plot(df2.ROC_50)
plt.show()

fig = plt.figure(figsize = (12,6))
plt.subplot(2, 1, 1)
plt.plot(df2.Momentum_50)
plt.axhline(y = 0, color = 'r')
plt.title('Momentum vs ROC')
plt.subplot(2, 1, 2)
plt.plot(df2.ROC_50)
plt.axhline(y = 0, color = 'r')
plt.show()

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df2['Momentum_50'], color = 'g', panel = 2),
        mpf.make_addplot(df2['ROC_50'], color = 'b', panel = 2),
        mpf.make_addplot(df2['Ignore'], color = 'r', panel = 2)
      ]
mpf.plot(df1, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df3 = df2.iloc[-30:-1,:]
ap1 = [ mpf.make_addplot(df3['Momentum_50'], color = 'g', panel = 2),
        mpf.make_addplot(df3['ROC_50'], color = 'b', panel = 2),
        mpf.make_addplot(df3['Ignore'], color = 'r', panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap1)