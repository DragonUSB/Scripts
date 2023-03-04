import pandas as pd
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

# Media Movil Simple
def MA(df, n):
    MA = pd.Series(pd.Series.rolling(df['Close'], n).mean(), name = 'MA_' + str(n))
    df = df.join(MA)
    return df

ma_50 = MA(datos, 50)
ma_200 = MA(ma_50, 200)

df = ma_200[['Close', 'MA_50', 'MA_200']]
df.plot(figsize = (12,6))

# Media Movil Exponencial
def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'], span = n, min_periods = n - 1, adjust = False).mean(), name = 'EMA_' + str(n))
    df = df.join(EMA)
    return df

df1 = EMA(datos, 50)
df2 = MA(df1, 50)
df3 = df2[['Close', 'MA_50', 'EMA_50']].copy()
df3.plot(figsize = (12, 6))

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df1['EMA_50'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df2['MA_50'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(df1, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df4 = df2.iloc[-30:-1,:]
ap1 = [ mpf.make_addplot(df4['EMA_50'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df4['MA_50'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(df4, type = 'candle', volume = True, style = 'binance', addplot = ap1)