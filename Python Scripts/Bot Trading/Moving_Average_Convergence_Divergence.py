import pandas as pd
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

# Moving Average Convergence Divergence
def MACD(df, f, s, sig):
    EMA1 = pd.Series(pd.Series.ewm(df['Close'], span = f, min_periods = f - 1, adjust = False).mean())
    EMA2 = pd.Series(pd.Series.ewm(df['Close'], span = s, min_periods = s - 1, adjust = False).mean())
    macd = EMA1 - EMA2
    MACD = pd.Series(macd, name = 'MACD')
    df = df.join(MACD)
    EMA3 = pd.Series(pd.Series.ewm(df['MACD'], span = sig, min_periods = sig - 1, adjust = False).mean(), name = 'Signal_Line')
    df = df.join(EMA3)
    hist = macd -EMA3
    HIST = pd.Series(hist, name = 'Histogram')
    df = df.join(HIST)
    y = pd.Series(datos['Ignore'], name = 'Y0')
    df = df.join(y)
    return df

df1 = MACD(datos, 12, 26, 9)
df2 = df1[['Close','MACD', 'Signal_Line', 'Histogram']].copy()
df2.plot(figsize = (12, 6))

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df1['MACD'], color = 'g', panel = 2),
        mpf.make_addplot(df1['Signal_Line'], color = 'b', panel = 2),
        mpf.make_addplot(df1['Histogram'], color = 'y', panel = 2),
        mpf.make_addplot(df1['Y0'], color = 'r', panel = 2)
      ]
mpf.plot(df1, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df3 = df1.iloc[-30:-1,:]
ap1 = [ mpf.make_addplot(df3['MACD'], color = 'g', panel = 2),
        mpf.make_addplot(df3['Signal_Line'], color = 'b', panel = 2),
        mpf.make_addplot(df3['Histogram'], color = 'y', panel = 2),
        mpf.make_addplot(df3['Y0'], color = 'r', panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap1)