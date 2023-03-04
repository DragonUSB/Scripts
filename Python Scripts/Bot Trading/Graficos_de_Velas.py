import pandas as pd
import mplfinance as mpf
import matplotlib.animation as animation
import plotly.graph_objects as go
from plotly.subplots import make_subplots

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos1 = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos1.set_index('Close_Timestamp', inplace = True)
datos1.index.name = 'Date'
datos1.Close.plot(rot = 45)

# Grafico con Plotly
fig = make_subplots(rows=2, cols=1, shared_xaxes = True, vertical_spacing = 0.02)

fig.append_trace(go.Candlestick(x = datos1.index,
                open = datos1['Open'],
                high = datos1['High'],
                low = datos1['Low'],
                close = datos1['Close']), row = 1, col = 1)

fig.append_trace(go.Bar(x = datos1.index, y = datos1.Volume), row = 2, col = 1)

fig.update_yaxes(title_text="Precio $", row=1, col=1)
fig.update_yaxes(title_text="Volume", row=2, col=1)

fig.update_layout(title_text = "UNI/USDT", xaxis_rangeslider_visible = False,
                  showlegend = False, hovermode = "x")

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=3, label="3m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(step="all")
                ])
            ),
            type="date"
        )
    )

fig.show()

# Grafico con mplfinance
mpf.plot(datos1, type = 'candle', volume = True, style = 'binance')

# Grafico con mplfinance acotando los dias
datos2 = datos1.iloc[-30:-1,:]
mpf.plot(datos2, type = 'candle', volume = True, style = 'binance')

# Animacion con mplfinance
# fig = mpf.figure(style = 'binance', figsize = (7, 8))
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(3, 1, 3)

# def animate(ival):
#     if (20 + ival) > len(datos1):
#         print('no more data to plot')
#         ani.event_source.interval *= 3
#         if ani.event_source.interval > 12000:
#             exit()
#         return
#     data = datos1.iloc[0:(20 + ival)]
#     ax1.clear()
#     ax2.clear()
#     mpf.plot(data, ax = ax1, volume = ax2, type = 'candle')

# ani = animation.FuncAnimation(fig, animate, interval = 250)

# #mpf.show()