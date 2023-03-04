import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

def ATR(df, n):
    df = df.reset_index()
    i = 0
    TR_l = [0]
    while i < df.index[-1]:
        TR = max(df.at[i + 1, 'High'], df.at[i, 'Close']) - min(df.at[i + 1, 'Low'], df.at[i, 'Close'])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    ATR = pd.Series(pd.Series.ewm(TR_s, span = n, min_periods = n).mean(), name = 'ATR_' + str(n))
    df = df.join(ATR)
    df.set_index('Close_Timestamp', inplace = True)
    return df

df = ATR(datos, 50)

fig = plt.figure(figsize = (12,6))
ax1 = plt.subplot(211)
plt.plot(df.Close)
plt.grid(True)
plt.title('Precio del UNI')    
ax1 = plt.subplot(212, sharex = ax1)
plt.plot(df.ATR_50, color = 'r')
plt.grid(True)
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_minor_locator(mdates.HourLocator(range(0, 25, 6)))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
plt.show()

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df['ATR_50'], color = 'g',panel=2),  # panel 2 specified
      ]
mpf.plot(df, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df1 = df.iloc[-30:-1,:]
ap1 = [ mpf.make_addplot(df1['ATR_50'], color = 'g',panel=2),  # panel 2 specified
      ]
mpf.plot(df1, type = 'candle', volume = True, style = 'binance', addplot = ap1)