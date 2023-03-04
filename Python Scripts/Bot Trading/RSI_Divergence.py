import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas_ta as ta
from datetime import datetime
from colorama import init, Back

plt.style.use('seaborn-darkgrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset = True)

datos = pd.read_csv('LUNAUSDT_1d.csv', sep = ",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']].copy()
datos.columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
datos = datos[datos['Volume'] != 0]
datos.reset_index(drop = True, inplace = True)
# datos.set_index('Close_Timestamp', inplace = True)

datos['RSI'] = datos.ta.rsi(length = 14)

def myRSI(price, n = 20):
    delta = price['Close'].diff()
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    RolUp = dUp.rolling(window = n).mean()
    RolDown = dDown.rolling(window = n).mean().abs()
    
    RS = RolUp / RolDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi

#datos['RSI'] = myRSI(datos)

#datos.dropna(inplace = True)
#datos.reset_index(drop = True, inplace = True)
print(datos.head(20))

datospl = datos[-360:-1]

fig = make_subplots(rows=2, cols=1)
fig.append_trace(go.Candlestick(x=datospl.index,
                open=datospl['Open'],
                high=datospl['High'],
                low=datospl['Low'],
                close=datospl['Close']), row=1, col=1)
fig.append_trace(go.Scatter(
    x=datospl.index,
    y=datospl['RSI'],
), row=2, col=1)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

def pivotid(datos1, l, n1, n2): #n1 n2 before and after candle l
    if (l - n1) < 0 or (l + n2) >= len(datos1):
        return 0
    
    pividLow=1
    pividHigh=1
    for i in range(l-n1, l+n2+1):
        if(datos1.Low[l]>datos1.Low[i]):
            pividLow=0
        if(datos1.High[l]<datos1.High[i]):
            pividHigh=0
    if pividLow and pividHigh:
        return 3
    elif pividLow:
        return 1
    elif pividHigh:
        return 2
    else:
        return 0

def RSIpivotid(datos1, l, n1, n2): #n1 n2 before and after candle l
    if l-n1 < 0 or l+n2 >= len(datos1):
        return 0

    pividLow=1
    pividHigh=1
    for i in range(l-n1, l+n2+1):
        if(datos1.RSI[l]>datos1.RSI[i]):
            pividLow=0
        if(datos1.RSI[l]<datos1.RSI[i]):
            pividHigh=0
    if pividLow and pividHigh:
        return 3
    elif pividLow:
        return 1
    elif pividHigh:
        return 2
    else:
        return 0 

#pivotid(datos,28145,5,5)

datos['pivot'] = datos.apply(lambda x: pivotid(datos, x.name, 5, 5), axis = 1)
datos['RSIpivot'] = datos.apply(lambda x: RSIpivotid(datos, x.name, 5, 5), axis = 1)

def pointpos(x):
    if x['pivot']==1:
        return x['Low']-1e-3
    elif x['pivot']==2:
        return x['High']+1e-3
    else:
        return np.nan

def RSIpointpos(x):
    if x['RSIpivot']==1:
        return x['RSI']-1
    elif x['RSIpivot']==2:
        return x['RSI']+1
    else:
        return np.nan

datos['pointpos'] = datos.apply(lambda row: pointpos(row), axis=1)
datos['RSIpointpos'] = datos.apply(lambda row: RSIpointpos(row), axis=1)
#datos[datos.RSIpivot==1].count()

datospl = datos[-360:-1]
fig = go.Figure(data=[go.Candlestick(x=datospl.index,
                open=datospl['Open'],
                high=datospl['High'],
                low=datospl['Low'],
                close=datospl['Close'])])

fig.add_scatter(x=datospl.index, y=datospl['pointpos'], mode="markers",
                marker=dict(size=5, color="MediumPurple"),
                name="pivot")
#fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

datospl = datos[-360:-1]
fig = make_subplots(rows=2, cols=1)
fig.append_trace(go.Candlestick(x=datospl.index,
                open=datospl['Open'],
                high=datospl['High'],
                low=datospl['Low'],
                close=datospl['Close']), row=1, col=1)

fig.add_scatter(x=datospl.index, y=datospl['pointpos'], mode="markers",
                marker=dict(size=4, color="MediumPurple"),
                name="pivot", row=1, col=1)

fig.append_trace(go.Scatter(x=datospl.index, y=datospl['RSI']), row=2, col=1)
fig.add_scatter(x=datospl.index, y=datospl['RSIpointpos'], mode="markers",
                marker=dict(size=4, color="MediumPurple"),
                name="pivot", row=2, col=1)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

print(datos)

backcandles= 90

#candleid = 8800
candleid = len(datos) - 1

maxim = np.array([])
minim = np.array([])
xxmin = np.array([])
xxmax = np.array([])

maximRSI = np.array([])
minimRSI = np.array([])
xxminRSI = np.array([])
xxmaxRSI = np.array([])

for i in range(candleid-backcandles, candleid+1):
    if datos.iloc[i].pivot == 1:
        minim = np.append(minim, datos.iloc[i].Low)
        xxmin = np.append(xxmin, i) #could be i instead datos.iloc[i].name
    if datos.iloc[i].pivot == 2:
        maxim = np.append(maxim, datos.iloc[i].High)
        xxmax = np.append(xxmax, i) # datos.iloc[i].name
    if datos.iloc[i].RSIpivot == 1:
        minimRSI = np.append(minimRSI, datos.iloc[i].RSI)
        xxminRSI = np.append(xxminRSI, datos.iloc[i].name)
    if datos.iloc[i].RSIpivot == 2:
        maximRSI = np.append(maximRSI, datos.iloc[i].RSI)
        xxmaxRSI = np.append(xxmaxRSI, datos.iloc[i].name)
        
slmin, intercmin = np.polyfit(xxmin, minim,1)
slmax, intercmax = np.polyfit(xxmax, maxim,1)
slminRSI, intercminRSI = np.polyfit(xxminRSI, minimRSI,1)
slmaxRSI, intercmaxRSI = np.polyfit(xxmaxRSI, maximRSI,1)

print(slmin, slmax, slminRSI, slmaxRSI)

datospl = datos[candleid-backcandles-5:candleid+backcandles]
fig = make_subplots(rows=2, cols=1)
fig.append_trace(go.Candlestick(x=datospl.index,
                open=datospl['Open'],
                high=datospl['High'],
                low=datospl['Low'],
                close=datospl['Close']), row=1, col=1)
fig.add_scatter(x=datospl.index, y=datospl['pointpos'], mode="markers",
                marker=dict(size=4, color="MediumPurple"),
                name="pivot", row=1, col=1)
fig.add_trace(go.Scatter(x=xxmin, y=slmin*xxmin + intercmin, mode='lines', name='min slope'), row=1, col=1)
fig.add_trace(go.Scatter(x=xxmax, y=slmax*xxmax + intercmax, mode='lines', name='max slope'), row=1, col=1)

fig.append_trace(go.Scatter(x=datospl.index, y=datospl['RSI']), row=2, col=1)
fig.add_scatter(x=datospl.index, y=datospl['RSIpointpos'], mode="markers",
                marker=dict(size=2, color="MediumPurple"),
                name="pivot", row=2, col=1)
fig.add_trace(go.Scatter(x=xxminRSI, y=slminRSI*xxminRSI + intercminRSI, mode='lines', name='min slope'), row=2, col=1)
fig.add_trace(go.Scatter(x=xxmaxRSI, y=slmaxRSI*xxmaxRSI + intercmaxRSI, mode='lines', name='max slope'), row=2, col=1)

fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()

# Fitting pivots into slopes
datospl = datos[-360:-1]
def divsignal(x, nbackcandles):
    backcandles=nbackcandles 
    candleid = int(x.name)

    maxim = np.array([])
    minim = np.array([])
    xxmin = np.array([])
    xxmax = np.array([])

    maximRSI = np.array([])
    minimRSI = np.array([])
    xxminRSI = np.array([])
    xxmaxRSI = np.array([])

    for i in range(candleid-backcandles, candleid+1):
        if datos.iloc[i].pivot == 1:
            minim = np.append(minim, datos.iloc[i].Low)
            xxmin = np.append(xxmin, i) #could be i instead datos.iloc[i].name
        if datos.iloc[i].pivot == 2:
            maxim = np.append(maxim, datos.iloc[i].High)
            xxmax = np.append(xxmax, i) # datos.iloc[i].name
        if datos.iloc[i].RSIpivot == 1:
            minimRSI = np.append(minimRSI, datos.iloc[i].RSI)
            xxminRSI = np.append(xxminRSI, datos.iloc[i].name)
        if datos.iloc[i].RSIpivot == 2:
            maximRSI = np.append(maximRSI, datos.iloc[i].RSI)
            xxmaxRSI = np.append(xxmaxRSI, datos.iloc[i].name)

    if maxim.size<2 or minim.size<2 or maximRSI.size<2 or minimRSI.size<2:
        return 0
    
    slmin, intercmin = np.polyfit(xxmin, minim,1)
    slmax, intercmax = np.polyfit(xxmax, maxim,1)
    slminRSI, intercminRSI = np.polyfit(xxminRSI, minimRSI,1)
    slmaxRSI, intercmaxRSI = np.polyfit(xxmaxRSI, maximRSI,1)
        
    if slmin > 1e-4 and slmax > 1e-4 and slmaxRSI <-0.1:
        return 1
    elif slmin < -1e-4 and slmax < -1e-4 and slminRSI > 0.1:
        return 2
    else:
        return 0

datospl['divSignal'] = datospl.apply(lambda row: divsignal(row,30), axis=1)

datospl[datospl.divSignal == 1].count()
print(datospl[datospl.divSignal == 1])

# pivot points levels instead of slopes
datospl = datos[-360:-1]
def divsignal2(x, nbackcandles):
    backcandles=nbackcandles 
    candleid = int(x.name)

    closp = np.array([])
    xxclos = np.array([])
    
    maxim = np.array([])
    minim = np.array([])
    xxmin = np.array([])
    xxmax = np.array([])

    maximRSI = np.array([])
    minimRSI = np.array([])
    xxminRSI = np.array([])
    xxmaxRSI = np.array([])

    for i in range(candleid-backcandles, candleid+1):
        closp = np.append(closp, datos.iloc[i].Close)
        xxclos = np.append(xxclos, i)
        if datos.iloc[i].pivot == 1:
            minim = np.append(minim, datos.iloc[i].Low)
            xxmin = np.append(xxmin, i) #could be i instead datos.iloc[i].name
        if datos.iloc[i].pivot == 2:
            maxim = np.append(maxim, datos.iloc[i].High)
            xxmax = np.append(xxmax, i) # datos.iloc[i].name
        if datos.iloc[i].RSIpivot == 1:
            minimRSI = np.append(minimRSI, datos.iloc[i].RSI)
            xxminRSI = np.append(xxminRSI, datos.iloc[i].name)
        if datos.iloc[i].RSIpivot == 2:
            maximRSI = np.append(maximRSI, datos.iloc[i].RSI)
            xxmaxRSI = np.append(xxmaxRSI, datos.iloc[i].name)

    slclos, interclos = np.polyfit(xxclos, closp,1)
    
    if slclos > 1e-4 and (maximRSI.size<2 or maxim.size<2):
        return 0
    if slclos < -1e-4 and (minimRSI.size<2 or minim.size<2):
        return 0
# signal decisions here !!!
    if slclos > 1e-4:
        if maximRSI[-1]<maximRSI[-2] and maxim[-1]>maxim[-2]:
            return 1
    elif slclos < -1e-4:
        if minimRSI[-1]>minimRSI[-2] and minim[-1]<minim[-2]:
            return 2
    else:
        return 0

datospl['divSignal2'] = datospl.apply(lambda row: divsignal2(row, 30), axis = 1)

datospl[datospl.divSignal2 == 2].count()
print(datospl[datospl.divSignal2 == 1])