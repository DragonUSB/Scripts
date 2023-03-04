import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot

datos = pd.read_csv('ETHUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

# Conversion Line
PH9 = datos['High'].rolling(window = 9).max()
PL9 = datos['Low'].rolling(window = 9).min()
datos['CL'] = (PH9 + PL9) / 2

# Base Line
PH26 = datos['High'].rolling(window = 26).max()
PL26 = datos['Low'].rolling(window = 26).min()
datos['BL'] = (PH26 + PL26) / 2

# Leading Span A
datos['LSA'] = ((datos['CL'] + datos['BL']) / 2).shift(26)

# Leading Span B
PH52 = datos['High'].rolling(window = 52).max()
PL52 = datos['Low'].rolling(window = 52).min()
datos['LSB'] = ((PH52 + PL52) / 2).shift(26)

# Leading Span
datos['LS'] = datos['Close'].shift(-26)

# split data into chunks where averages cross each other
datos1 = datos.copy()
datos1['label'] = np.where(datos1['LSA'] > datos1['LSB'], 1, 0)
datos1['group'] = datos1['label'].ne(datos1['label'].shift()).cumsum()
datos1 = datos1.groupby('group')
dfs = []
for name, data in datos1:
    dfs.append(data)

# custom function to set fill color
def fillcol(label):
    if label >= 1:
        return 'rgba(0,250,0,0.4)'
    else:
        return 'rgba(250,0,0,0.4)'

# Plot
fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(datos.index, datos.Close)
# plt.plot(datos.index, datos.CL, label = 'Conversion Line')
# plt.plot(datos.index, datos.BL, label = 'Base Line')
plt.plot(datos.index, datos.LSA, label = 'Leading Span A', color = 'green')
plt.plot(datos.index, datos.LSB, label = 'Leading Span B', color = 'red')
# plt.plot(datos.index, datos.LS, label = 'Lagging Span')
plt.fill_between(datos.index, datos.LSA, datos.LSB, where=datos.LSA >= datos.LSB, color='lightgreen')
plt.fill_between(datos.index, datos.LSA, datos.LSB, where=datos.LSA < datos.LSB, color='lightcoral')
plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()

# Set colours for up and down candles
INCREASING_COLOR = '#17BECF'
DECREASING_COLOR = '#7F7F7F'

# create list to hold dictionary with data for our first series to plot
# (which is the candlestick element itself)
data1 = [dict(
    type = 'candlestick',
    open = datos.Open,
    high = datos.High,
    low = datos.Low,
    close = datos.Close,
    x = datos.index,
    yaxis = 'y2',
    name = 'F',
    increasing = dict(line = dict(color = INCREASING_COLOR)),
    decreasing = dict(line = dict(color = DECREASING_COLOR)),
)]

# Create empty dictionary for later use to hold settings and layout options
layout = dict()

# create our main chart "Figure" object which consists of data to plot and layout settings
fig = dict(data = data1, layout = layout)

# Assign various seeting and choices - background colour, range selector etc
fig['layout']['plot_bgcolor'] = 'rgb(250, 250, 250)'
fig['layout']['xaxis'] = dict(rangeselector = dict( visible = True))
fig['layout']['yaxis'] = dict(domain = [0, 0.1], showticklabels = False)
fig['layout']['yaxis2'] = dict(domain = [0.1, 0.9])
fig['layout']['legend'] = dict(orientation = 'h', y = 0.9, x = 0.3, yanchor = 'bottom')
fig['layout']['margin'] = dict(t = 40, b = 40, r = 40, l = 40)

# Populate the "rangeselector" object with necessary settings
rangeselector=dict(
    visible = True,
    x = 0, y = 0.9,
    bgcolor = 'rgba(150, 200, 250, 0.4)',
    font = dict( size = 13 ),
    buttons = list([
        dict(count = 1, label = 'reset', step = 'all'),
        dict(count = 1, label = '1yr', step = 'year', stepmode = 'backward'),
        dict(count = 9, label = '9 mo', step = 'month', stepmode = 'backward'),
        dict(count = 6, label = '6 mo', step = 'month', stepmode = 'backward'),
        dict(count = 3, label = '3 mo', step = 'month', stepmode = 'backward'),
        dict(count = 1, label = '1 mo', step = 'month', stepmode = 'backward'),
        dict(step = 'all')
    ]))
    
fig['layout']['xaxis']['rangeselector'] = rangeselector

for datos1 in dfs:
    fig['data'].append(dict(x = datos1.index, y = datos1.LSA, type ='scatter', mode ='lines',
                            line = dict(color = 'rgba(0,0,0,0)'), showlegend = False,
                            yaxis = 'y2'))
    
    fig['data'].append(dict(x = datos1.index, y = datos1.LSB, type ='scatter', mode ='lines',
                            line = dict(color = 'rgba(0,0,0,0)'), showlegend = False,
                            yaxis = 'y2', fill = 'tonexty', 
                            fillcolor = fillcol(datos1['label'].iloc[0])))

# Append the Ichimoku elements to the plot
fig['data'].append(dict(x = datos.index, y = datos['CL'], type = 'scatter', mode = 'lines', 
                        line = dict(width = 1),
                        marker = dict(color = '#33BDFF'),
                        yaxis = 'y2', name = 'Conversion Line'))
fig['data'].append(dict(x = datos.index, y = datos['BL'], type = 'scatter', mode = 'lines', 
                        line = dict(width = 1),
                        marker = dict(color = '#F1F316'),
                        yaxis = 'y2', name = 'Base Line'))
fig['data'].append(dict(x = datos.index, y = datos['LSA'], type = 'scatter', mode = 'lines', 
                        line = dict(width = 1), 
                        marker = dict(color = '#228B22'),
                        yaxis = 'y2', name = 'Leading Span A'))
fig['data'].append(dict(x = datos.index, y = datos['LSB'], type = 'scatter', mode = 'lines', 
                        line = dict(width = 1),
                        marker = dict(color = '#FF3342'),
                        yaxis = 'y2', name = 'Leading Span B'))
fig['data'].append(dict(x = datos.index, y = datos['LS'], type = 'scatter', mode = 'lines', 
                        line = dict(width = 1),
                        marker = dict(color = '#D105F5'),
                        yaxis = 'y2', name = 'Lagging Span'))

# Set colour list for candlesticks
colors = []
for i in range(len(datos.Close)):
    if i != 0:
        if datos.Close[i] > datos.Close[i-1]:
            colors.append(INCREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)
    else:
        colors.append(DECREASING_COLOR)
        
plot(fig, filename = 'candlestick-ichimoku.html')

datos.dropna(inplace=True)
datos['above_cloud'] = 0
datos['above_cloud'] = np.where((datos['Low'] > datos['LSA']) & (datos['Low'] > datos['LSB'] ), 1, datos['above_cloud'])
datos['above_cloud'] = np.where((datos['High'] < datos['LSA']) & (datos['High'] < datos['LSB']), -1, datos['above_cloud'])
datos['A_above_B'] = np.where((datos['LSA'] > datos['LSB']), 1, -1)
datos['tenkan_kiju_cross'] = np.NaN
datos['tenkan_kiju_cross'] = np.where((datos['CL'].shift(1) <= datos['BL'].shift(1)) & (datos['CL'] > datos['BL']), 1, datos['tenkan_kiju_cross'])
datos['tenkan_kiju_cross'] = np.where((datos['CL'].shift(1) >= datos['BL'].shift(1)) & (datos['CL'] < datos['BL']), -1, datos['tenkan_kiju_cross'])

# Estrategia 1
# datos['price_tenkan_cross'] = np.NaN
# datos['price_tenkan_cross'] = np.where((datos['Open'].shift(1) <= datos['CL'].shift(1)) & (datos['Open'] > datos['CL']), 1, datos['price_tenkan_cross'])
# datos['price_tenkan_cross'] = np.where((datos['Open'].shift(1) >= datos['CL'].shift(1)) & (datos['Open'] < datos['CL']), -1, datos['price_tenkan_cross'])
# datos['buy'] = np.NaN
# datos['buy'] = np.where((datos['above_cloud'].shift(1) == 1) & (datos['A_above_B'].shift(1) == 1) & ((datos['tenkan_kiju_cross'].shift(1) == 1) | (datos['price_tenkan_cross'].shift(1) == 1)), 1, datos['buy'])
# datos['buy'] = np.where(datos['tenkan_kiju_cross'].shift(1) == -1, 0, datos['buy'])
# datos['buy'].ffill(inplace=True)
# datos['sell'] = np.NaN
# datos['sell'] = np.where((datos['above_cloud'].shift(1) == -1) & (datos['A_above_B'].shift(1) == -1) & ((datos['tenkan_kiju_cross'].shift(1) == -1) | (datos['price_tenkan_cross'].shift(1) == -1)), -1, datos['sell'])
# datos['sell'] = np.where(datos['tenkan_kiju_cross'].shift(1) == 1, 0, datos['sell'])
# datos['sell'].ffill(inplace=True)

# Estrategia 2
datos['buy'] = np.NaN
datos['buy'] = np.where((datos['above_cloud'].shift(1) == 1) & (datos['A_above_B'].shift(1) == 1) & (datos['tenkan_kiju_cross'].shift(1) == 1), 1, datos['buy'])
datos['buy'] = np.where(datos['tenkan_kiju_cross'].shift(1) == -1, 0, datos['buy'])
datos['buy'].ffill(inplace=True)
datos['sell'] = np.NaN
datos['sell'] = np.where(datos['tenkan_kiju_cross'].shift(1) == -1, -1, datos['sell'])
datos['sell'] = np.where(datos['tenkan_kiju_cross'].shift(1) == 1, 0, datos['sell'])
datos['sell'].ffill(inplace=True)

datos['position'] = datos['buy'] + datos['sell']
datos['position'].plot(figsize=(12,6))
datos['stock_returns'] = np.log(datos['Open']) - np.log(datos['Open'].shift(1))
datos['strategy_returns'] = datos['stock_returns'] * datos['position']
datos[['stock_returns', 'strategy_returns']].cumsum().plot(figsize=(12,6))
plt.show()