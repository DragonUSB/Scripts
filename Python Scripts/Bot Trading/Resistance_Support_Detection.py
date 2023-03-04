import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime
from colorama import init, Back

plt.style.use('seaborn-darkgrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset = True)

datos = pd.read_csv('BTCUSDT_1d.csv', sep = ",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume', 'Ignore']].copy()
datos = datos[datos['Volume'] != 0]
datos.reset_index(drop = True, inplace = True)
# datos.set_index('Close_Timestamp', inplace = True)

# Support and Resitance FUNCTIONS

def support(df, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l - n1 + 1, l + 1):
        if (df.Low[i] > df.Low[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if (df.Low[i] < df.Low[i - 1]):
            return 0
    return 1

# print(support(datos, 46, 3, 2))

def resistance(df, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l - n1 + 1, l + 1):
        if(df.High[i] < df.High[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if(df.High[i] > df.High[i - 1]):
            return 0
    return 1

# print(resistance(datos, 30, 3, 5))

# datos1 = datos[0:50]

# fig = go.Figure(data = [go.Candlestick(x = datos1.index,
#                 open = datos1['Open'],
#                 high = datos1['High'],
#                 low = datos1['Low'],
#                 close = datos1['Close'])])
# fig.show()

# sr = []
# n1 = 3
# n2 = 2
# for row in range(3, 205): #len(df)-n2
#     if support(datos, row, n1, n2):
#         sr.append((row, datos.Low[row], 1))
#     if resistance(datos, row, n1, n2):
#         sr.append((row, datos.High[row], 2))
# print(sr)

# s = 0
# e = 200
# datos2 = datos[s:e]

# fig = go.Figure(data = [go.Candlestick(x = datos2.index,
#                 open = datos2['Open'],
#                 high = datos2['High'],
#                 low = datos2['Low'],
#                 close = datos2['Close'])])

# c = 0
# while (1):
#     if(c > len(sr)-1): #or sr[c][0]>e
#         break
#     fig.add_shape(type = 'line', x0 = s, y0 = sr[c][1],
#                   x1 = e,
#                   y1 = sr[c][1]
#                   ) #x0=sr[c][0]-5 x1=sr[c][0]+5
#     c += 1
# fig.show()

# plotlist1 = [x[1] for x in sr if x[2] == 1]
# plotlist2 = [x[1] for x in sr if x[2] == 2]
# plotlist1.sort()
# plotlist2.sort()

# for i in range(1, len(plotlist1)):
#     if(i >= len(plotlist1)):
#         break
#     if abs(plotlist1[i] - plotlist1[i - 1]) <= 0.005:
#         plotlist1.pop(i)

# for i in range(1, len(plotlist2)):
#     if(i >= len(plotlist2)):
#         break
#     if abs(plotlist2[i] - plotlist2[i - 1]) <= 0.005:
#         plotlist2.pop(i)
# plotlist2
# #plt.hist(plotlist, bins = 10, alpha = 0.5)

# s = 0
# e = 200
# datos3 = datos[s:e]

# fig = go.Figure(data = [go.Candlestick(x = datos3.index,
#                 open = datos3['Open'],
#                 high = datos3['High'],
#                 low = datos3['Low'],
#                 close = datos3['Close'])])

# c = 0
# while (1):
#     if(c > len(plotlist1) - 1): #or sr[c][0]>e
#         break
#     fig.add_shape(type = 'line', x0 = s, y0 = plotlist1[c],
#                   x1 = e,
#                   y1 = plotlist1[c],
#                   line = dict(color = "MediumPurple", width = 3)
#                   )
#     c += 1

# c = 0
# while (1):
#     if(c > len(plotlist2) - 1): #or sr[c][0]>e
#         break
#     fig.add_shape(type = 'line', x0 = s, y0 = plotlist2[c],
#                   x1 = e,
#                   y1 = plotlist2[c],
#                   line = dict(color = "RoyalBlue", width = 1)
#                   )
#     c += 1

# fig.show()

ss = []
rr = []
n1 = 3
n2 = 3
for row in range(int(len(datos) / 2), len(datos) - n2): #len(df)-n2
    if support(datos, row, n1, n2):
        ss.append((datos.Close_Timestamp[row], datos.Low[row]))
    if resistance(datos, row, n1, n2):
        rr.append((datos.Close_Timestamp[row], datos.High[row]))

s = int(len(datos) / 2)
e = len(datos) 
datos4 = datos[s:e]
e = datos.Close_Timestamp[e - 1]
datos.set_index('Close_Timestamp', inplace = True)
datos4.set_index('Close_Timestamp', inplace = True)

fig = go.Figure(data = [go.Candlestick(x = datos.index,
                open = datos['Open'],
                high = datos['High'],
                low = datos['Low'],
                close = datos['Close'])])

c = 0
while (1):
    if(c > len(ss)-1):
        break
    fig.add_shape(type = 'line', x0 = ss[c][0], y0 = ss[c][1],
                  x1 = e,
                  y1 = ss[c][1],
                  line = dict(color = "MediumPurple", width = 3)
                  )
    c += 1

c = 0
while (1):
    if(c > len(rr)-1):
        break
    fig.add_shape(type = 'line', x0 = rr[c][0], y0 = rr[c][1],
                  x1 = e,
                  y1 = rr[c][1],
                  line = dict(color = "RoyalBlue", width = 1)
                  )
    c += 1    

fig.show()