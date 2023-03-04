import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

datos = pd.read_csv('UNIUSDT_4h.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

# ////// User input //////

MAtype = 'SMA'
MAlen = 20
BBlen = 20
BBmult = 2
RSIlen = 14
RSIn = 50
RSInlen = 10
SLenable = False
REenter = False
SLprct = 6.0
source = datos

# ////// In-built indicators //////

# RSI
def RSI(df, n):
    df['diff'] = df.Close.diff(periods = 1)
    df.dropna(inplace = True)
    df['sub'] = df['diff'][df['diff'] > 0]
    df['baj'] = abs(df['diff'][df['diff'] <= 0])
    df.fillna(value = 0, inplace = True)
    media_sub = df['sub'].rolling(window = n).mean()
    media_baj = df['baj'].rolling(window = n).mean()
    RSI = pd.Series(100 - (100 / (1 + (media_sub / media_baj))), name = 'RSI')
    df = df.join(RSI)
    df.drop(columns = ['diff','sub','baj'], inplace=True)
    return df

# Bollinger Bands
def BBANDS(df, n, m, p):
    # MA = pd.Series(pd.Series.rolling(df['Close'], n).mean())
    MA = pd.Series(pd.Series.ewm(df['Close'], span = n, min_periods = n - 1, adjust = False).mean())
    MA = pd.Series(MA, name = 'MA')
    df = df.join(MA)
    MSD = pd.Series(pd.Series.rolling(df['Close'], m).std())
    b1 = MA + (MSD * p)
    B1 = pd.Series(b1, name = 'BBupper')
    df = df.join(B1)
    b2 = MA - (MSD * p)
    B2 = pd.Series(b2, name = 'BBlower')
    df = df.join(B2)
    return df

# Crossover
def crossover(series1, series2):
    crossover = (series1 < series2) & (series1.shift(-1) > series2.shift(-1))
    return crossover

# Crossunder
def crossunder(series1, series2):
    crossunder = (series1 > series2) & (series1.shift(-1) < series2.shift(-1))
    return crossunder

source = RSI(source, RSIlen)
source = BBANDS(source, MAlen, BBlen, BBmult)

# ////// Signals calculations & combined validation //////

# // Bollinger Bands
source['BBbull'] = (source.Open < source.BBlower) & (source.Close > source.BBlower)
source['BBbear'] = (source.Open > source.BBupper) & (source.Close < source.BBupper)

# // Relative Strenght Index
source['RSIn'] = pd.Series(source.Close * 0 + RSIn, name = 'RSIn')
source['RSIcrossover'] = crossover(source.RSI, source.RSIn)
source['RSIcrossunder'] = crossunder(source.RSI, source.RSIn)

source['RSIbull'] = False
source['RSIbear'] = False
for j in range(RSInlen, len(source)):
    for i in range(0, RSInlen):
        if source.RSIcrossover[j - i] == True:
            source['RSIbull'][j] = True
    for i in range(0, RSInlen):
        if source.RSIcrossunder[j - i] == True:
            source['RSIbear'][j] = True

# // Combined validation
source['longsignal']  = source.BBbull & source.RSIbull
source['shortsignal'] = source.BBbear & source.RSIbear

# ////// Determine first signal direction change //////

source['lastsignalislong'] = np.where(source.longsignal, True, False)
source['lastsignalisshort'] = np.where(source.shortsignal, True, False)

source['newtradedirection'] = np.where(((source['lastsignalislong'] == True) & (source['lastsignalislong'].shift(1) == False)) | ((source['lastsignalisshort'] == True) & (source['lastsignalisshort'].shift(1) == False)), True, False)

# ////// SL calculations and value storing //////

source['longSL']  = source.Close - source.Close * SLprct / 100
source['shortSL'] = source.Close + source.Close * SLprct / 100

source['SLlongsaved'] = np.where(source.longsignal & source.newtradedirection | source.longsignal, source.longSL, np.nan)
source['SLshortsaved'] = np.where(source.shortsignal & source.newtradedirection | source.shortsignal, source.shortSL, np.nan)

source['longsignal'] = np.where(source.longsignal, source.Close - source.Close * 3 / 100, np.nan)
source['shortsignal'] = np.where(source.shortsignal, source.Close + source.Close * 3 / 100, np.nan)

# print(source)

# ////// Plots to the chart //////

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(source.index, source.Close)

# // Signals
plt.scatter(x = source.index, y = source.longsignal, marker = '^', color = '#3064fc', label = 'Long Signal')
plt.scatter(x = source.index, y = source.shortsignal, marker = 'v', color = '#fc1049', label = 'Short Signal')

# // Stop Losses
plt.scatter(x = source.index, y = source.SLlongsaved, label = 'Long SL', color = 'blue', marker = '^')
plt.scatter(x = source.index, y = source.SLshortsaved, label = 'Short SL', color = 'red', marker = 'v')

# // Bollinger Bands
plt.plot(source.MA, color = 'black', label = 'Moving Average')
plt.plot(source.BBupper, label = 'Upper Bound', color = 'gray')
plt.plot(source.BBlower, label = 'Lower Bound', color = 'gray')
plt.fill_between(source.index, source.BBupper, source.BBlower, color = 'gray', alpha = 0.1, interpolate = True)

plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()

# Grafico con Plotly
fig = make_subplots(rows = 3, cols = 1, shared_xaxes = True, vertical_spacing = 0.02)

fig.append_trace(go.Candlestick(x = source.index,
                open = source['Open'],
                high = source['High'],
                low = source['Low'],
                close = source['Close']), row = 1, col = 1)

fig.append_trace(go.Bar(x = source.index, y = source.Volume), row = 2, col = 1)

fig.append_trace(go.Scatter(x = source.index, y = source.MA, line = dict(color = 'black'), mode = "lines"), row = 1, col = 1)

fig.append_trace(go.Scatter(x = source.index, y = source.BBupper, line = dict(color = 'gray'), mode = "lines"), row = 1, col = 1)

fig.append_trace(go.Scatter(x = source.index, y = source.BBlower, line = dict(color = 'gray'), fill='tonexty', mode = "lines"), row = 1, col = 1)

fig.append_trace(go.Scatter(x = source.index, y = source.longsignal, mode = 'markers', marker_color = '#3064fc', marker_symbol = 'triangle-up', marker_size = 10), row = 3, col = 1)

fig.append_trace(go.Scatter(x = source.index, y = source.shortsignal, mode = 'markers', marker_color = '#fc1049', marker_symbol = 'triangle-down', marker_size = 10), row = 3, col = 1)

fig.update_yaxes(title_text ="Precio $", row = 1, col = 1)
fig.update_yaxes(title_text = "Volume", row = 2, col = 1)
fig.update_yaxes(title_text = "Signals", row = 3, col = 1)

fig.update_layout(title_text = "UNI/USDT", xaxis_rangeslider_visible = False,
                  showlegend = False, hovermode = "x")

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
                dict(count = 3, label = "3m", step = "month", stepmode = "backward"),
                dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
                dict(count = 9, label = "9m", step = "month", stepmode = "backward"),
                dict(count = 1, label = "1y", step = "year", stepmode = "backward"),
                dict(count = 1, label = "YTD", step = "year", stepmode = "todate"),
                dict(step = "all")
                ])
            ),
            type = "date"
        )
    )

fig.show()

# ////// Strategy Entry & Exit //////

# // Longs
# if source['longsignal']  and newtradedirection
#     strategy.entry(id="Long"           ,long=True)
# strategy.exit     (id="Long exit1"  ,from_entry="Long",
#  limit = newtradedirection ? BBupper : na, 
#  stop  = SLenable ? SLlongsaved  : na,
#  when  = strategy.position_size > 0)

# if source['longsignal']  and strategy.position_size == 0 and REenter
#     strategy.entry(id="Long after SL"  ,long=True)
# strategy.exit     (id="Long exit2"  ,from_entry="Long after SL",
#  limit = newtradedirection ? BBupper : na,
#  stop  = SLenable ? SLlongsaved  : na,
#  when  = strategy.position_size > 0)

# // Shorts
# if shortsignal and newtradedirection
#     strategy.entry(id="Short"          ,long=False)
# strategy.exit     (id="Short exit1" ,from_entry="Short",
#  limit = newtradedirection ? BBlower      : na,
#  stop  = SLenable          ? SLshortsaved : na, 
#  when  = strategy.position_size < 0)

# if shortsignal and strategy.position_size == 0 and REenter
#     strategy.entry(id="Short after SL" ,long=False)
# strategy.exit     (id="Short exit2" ,from_entry="Short after SL",
#  limit = newtradedirection ? BBlower      : na,
#  stop  = SLenable          ? SLshortsaved : na,
#  when  = strategy.position_size < 0)