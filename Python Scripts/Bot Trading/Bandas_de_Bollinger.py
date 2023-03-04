import pandas as pd
import mplfinance as mpf

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.Close.plot(rot = 45)

def BBANDS(df, n):
    MA = pd.Series(pd.Series.rolling(df['Close'], n).mean())
    MSD = pd.Series(pd.Series.rolling(df['Close'], n).std())
    b1 = MA + (MSD*2)
    B1 = pd.Series(b1, name = 'BB_' + str(n))
    df = df.join(B1)
    b2 = MA - (MSD*2)
    B2 = pd.Series(b2, name = 'Bb_' + str(n))
    df = df.join(B2)
    return df

df1 = BBANDS(datos, 20)
df2 = df1[['Close', 'BB_20', 'Bb_20']]
df2.plot(figsize = (12, 6))

Bpor = pd.Series((df2.Close - df2.Bb_20) / (df2.BB_20 - df2.Bb_20), name = 'Bpor')
df1 = df1.join(Bpor)

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df1['BB_20'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df1['Bb_20'], color = 'b'),  # uses panel 0 by default
        mpf.make_addplot(df1['Bpor'], color = 'r',  panel = 2)
      ]
mpf.plot(df1, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df3 = df1.iloc[-120:-1,:]
ap1 = [ mpf.make_addplot(df3['BB_20'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(df3['Bb_20'], color = 'b'),  # uses panel 0 by default
        mpf.make_addplot(df3['Bpor'], color = 'r',  panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap1)