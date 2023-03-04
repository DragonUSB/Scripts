import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
# datos.Close.plot(rot = 45)

# RSI
def RSI(df, n):
    df['diff']=df.Close.diff(periods=1)
    df.dropna(inplace=True)
    df['sub'] = df['diff'][df['diff'] > 0]
    df['baj'] = abs(df['diff'][df['diff'] <= 0])
    df.fillna(value = 0, inplace=True)
    media_sub = df['sub'].rolling(window = n).mean()
    media_baj = df['baj'].rolling(window = n).mean()
    RSI= pd.Series(100 - (100 / (1 + (media_sub / media_baj))), name = 'RSI_' + str(n))
    df = df.join(RSI)
    df.drop(columns = ['diff','sub','baj'], inplace=True)
    return df

df2 = RSI(datos, 14)
Nivel_30 = pd.Series(df2['Ignore'] + 30, name = 'Nivel_30')
Nivel_70 = pd.Series(df2['Ignore'] + 70, name = 'Nivel_70')
df2 = df2.join(Nivel_30)
df2 = df2.join(Nivel_70)

fig = plt.figure(figsize = (12, 6))
plt.subplot(2, 1, 1)
plt.plot(df2.Close)
plt.title('Precio del UNI')
plt.subplot(2, 1, 2)
plt.plot(df2.RSI_14)
plt.plot(df2.Nivel_30, color = 'r')
plt.plot(df2.Nivel_70, color = 'r')
plt.show()

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(df2['RSI_14'], color = 'b', panel = 2),
        mpf.make_addplot(df2['Nivel_30'], color = 'r', panel = 2),
        mpf.make_addplot(df2['Nivel_70'], color = 'r', panel = 2)
      ]
mpf.plot(df2, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
df3 = df2.iloc[-120:-1,:]
ap1 = [ mpf.make_addplot(df3['RSI_14'], color = 'b', panel = 2),
        mpf.make_addplot(df3['Nivel_30'], color = 'r', panel = 2),
        mpf.make_addplot(df3['Nivel_70'], color = 'r', panel = 2)
      ]
mpf.plot(df3, type = 'candle', volume = True, style = 'binance', addplot = ap1)

# Grafico con Plotly
fig = make_subplots(rows = 3, cols = 1, shared_xaxes = True, vertical_spacing = 0.02)

fig.append_trace(go.Candlestick(x = df2.index,
                open = df2['Open'],
                high = df2['High'],
                low = df2['Low'],
                close = df2['Close']), row = 1, col = 1)

fig.append_trace(go.Bar(x = df2.index, y = df2.Volume), row = 2, col = 1)

fig.append_trace(go.Scatter(x = df2.index, y = df2.RSI_14, mode = "lines"), row = 3, col = 1)

fig.append_trace(go.Scatter(x = df2.index, y = df2.Nivel_30, mode = "lines"), row = 3, col = 1)

fig.append_trace(go.Scatter(x = df2.index, y = df2.Nivel_70, mode = "lines"), row = 3, col = 1)

fig.update_yaxes(title_text ="Precio $", row = 1, col = 1)
fig.update_yaxes(title_text = "Volume", row = 2, col = 1, autorange = True)
fig.update_yaxes(title_text = "RSI", row = 3, col = 1)

fig.update_layout(title_text = "UNI/USDT", xaxis_rangeslider_visible = False,
                  showlegend = False, hovermode = "x")

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
                dict(count = 3, label = "3m", step = "month", stepmode = "backward"),
                dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
                dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
                dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
                dict(step = "all")
                ])
            ),
            type = "date"
        )
    )

fig.show()