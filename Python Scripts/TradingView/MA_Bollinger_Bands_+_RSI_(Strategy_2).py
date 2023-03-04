from pickle import FALSE
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

datos = pd.read_csv('LUNAUSDT_1h.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

# ////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////   INPUTS   /////////////////I/////////////////
# ////////////////////////////////////////////////////////////////////////////////

source = datos

LongTrades = True
ShortTrades = True
REenter = False

SLenable = False
SLprct = 5.0
TrailStop = False
ATRX = 10.0
ATRlen = 14   

BBX = 2.0
BBlen = 200
MAlen = 200
MAtype = "SMA"

RSINlen = 10
RSIN = 50
RSIlen = 6

UseVol = False
AddVol = False
BBvolX = 5.0
baselen = 2000

UseDateFilter  = False
# StartDate      = timestamp("1 Jan 2000 00:00 +0000")
# EndDate        = timestamp("1 Jan 2100 00:00 +0000")
UseTimeFilter  = False
# TradingSession = "1000-2200:1234567"

# ////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////   SIGNALS   /////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

# ////////////////// Bollinger Bands //////////////////

def BBANDS(df, n, m, p):
    # MA = pd.Series(pd.Series.rolling(df['Close'], n).mean())
    EMA = pd.Series(pd.Series.ewm(df['Close'], span = n, min_periods = n - 1, adjust = False).mean())
    EMA = pd.Series(EMA, name = 'EMA')
    df = df.join(EMA)
    MSD = pd.Series(pd.Series.rolling(df['Close'], m).std())
    b1 = EMA + (MSD * p)
    B1 = pd.Series(b1, name = 'BBupper')
    df = df.join(B1)
    b2 = EMA - (MSD * p)
    B2 = pd.Series(b2, name = 'BBlower')
    df = df.join(B2)
    return df

source = BBANDS(source, MAlen, BBlen, BBX)

source['BBbull'] = (source.Open < source.BBlower) & (source.Close > source.BBlower)
source['BBbear'] = (source.Open > source.BBupper) & (source.Close < source.BBupper)

# ////////////////// Relative Strength Index //////////////////

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

# Crossover
def crossover(series1, series2):
    crossover = (series1 < series2) & (series1.shift(-1) > series2.shift(-1))
    return crossover

# Crossunder
def crossunder(series1, series2):
    crossunder = (series1 > series2) & (series1.shift(-1) < series2.shift(-1))
    return crossunder

source = RSI(source, RSIlen)

source['RSIN'] = pd.Series(source.Close * 0 + RSIN, name = 'RSIN')
source['RSIcrossover'] = crossover(source.RSI, source.RSIN)
source['RSIcrossunder'] = crossunder(source.RSI, source.RSIN)

source['RSIbull'] = False
source['RSIbear'] = False
for j in range(RSINlen, len(source)):
    for i in range(0, RSINlen):
        if source.RSIcrossover[j - i] == True:
            source['RSIbull'][j] = True
    for i in range(0, RSINlen):
        if source.RSIcrossunder[j - i] == True:
            source['RSIbear'][j] = True

# ////////////////// Volatility //////////////////

def SMA(df, n, name):
    SMA = pd.Series(pd.Series.rolling(df['BBvol'], n).mean(), name = name)
    df = df.join(SMA)
    return df

source['BBvol'] = source['BBupper'] - source['BBlower']
source = SMA(source, 50, 'SignalLine')
source = SMA(source, 2000, 'BaseLine')
source['HighVolLvl'] = source['BaseLine'] + source['BaseLine'] * BBvolX / 10
source['LowVolLvl'] = source['BaseLine'] - source['BaseLine'] * BBvolX / 10

source['volExtrmHigh'] =np.where((source['BBvol'] > source['HighVolLvl']) & UseVol, True, False)
source['volExtrmLow'] =np.where((source['BBvol'] > source['LowVolLvl']) & UseVol, True, False)

# ////////////////// Date and Time //////////////////

# In(t)      => na(time(timeframe.period, t)) == false
# TimeFilter = (UseTimeFilter and not In(TradingSession)) or not UseTimeFilter
# DateFilter = time >= StartDate and time <= EndDate

# DateTime = (UseDateFilter ? not DateFilter : true) and (UseTimeFilter ? In(TradingSession) : true) 

# ////////////////// Combined validation //////////////////

# longsignal  = BBbull and RSIbull and not volExtrmHigh and DateTime
# shortsignal = BBbear and RSIbear and not volExtrmHigh and DateTime

source['longsignal']  = source.BBbull & source.RSIbull & ~source['volExtrmHigh']
source['shortsignal'] = source.BBbear & source.RSIbear & ~source['volExtrmHigh']

source['longsignalonly'] = source['longsignal'] & LongTrades
source['shortsignalonly'] = source['shortsignal'] & ShortTrades

# ////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////   STOP LOSSES    ///////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

# ////////////////// Determine Signal Direction Change //////////////////

source['lastsignalislong'] = np.where(source.longsignal, True, False)
source['lastsignalisshort'] = np.where(source.shortsignal, True, False)

source['newtradedirection'] = np.where(((source['lastsignalislong'] == True) & (source['lastsignalislong'].shift(1) == False)) | ((source['lastsignalisshort'] == True) & (source['lastsignalisshort'].shift(1) == False)), True, False)

# ////////////////// Stop losses calculations //////////////////

# // MAE Stop

source['LongSL']  = source.Close - source.Close * SLprct / 100
source['ShortSL'] = source.Close + source.Close * SLprct / 100

# // Trailing Stop

def ATR(df, n):
    df = df.reset_index()
    i = 0
    TR_l = [0]
    while i < df.index[-1]:
        TR = max(df.at[i + 1, 'High'], df.at[i, 'Close']) - min(df.at[i + 1, 'Low'], df.at[i, 'Close'])
        TR_l.append(TR)
        i = i + 1
    TR_s = pd.Series(TR_l)
    ATR = pd.Series(pd.Series.ewm(TR_s, span = n, min_periods = n).mean(), name = 'ATR')
    df = df.join(ATR)
    df.set_index('Close_Timestamp', inplace = True)
    return df

source = ATR(source, ATRlen)
source['Stop'] = ATRX * source['ATR']
source['LongTrailSL'] = source['Close'] - source['Stop']
source['ShortTrailSL'] = source['Close'] + source['Stop']

# ////////////////// Stop Loss value storing //////////////////

# // Long Stops

source['LongEntryPrice'] = np.where(source.longsignal & source.newtradedirection | source.longsignal, source.Close, np.nan)
source['SLlongsaved'] = np.where((source.longsignal & source.newtradedirection | source.longsignal) & (SLenable & (not TrailStop)), source.LongSL, np.nan)
source['TrailSLlongsaved'] = np.where((source.longsignal & source.newtradedirection | source.longsignal) & TrailStop, source.LongTrailSL, np.nan)

# // Short Stops

source['ShortEntryPrice'] = np.where(source.shortsignal & source.newtradedirection | source.shortsignal, source.Close, np.nan)
source['SLshortsaved'] = np.where((source.shortsignal & source.newtradedirection | source.shortsignal) & (SLenable & (not TrailStop)), source.ShortSL, np.nan)
source['TrailSLshortsaved'] = np.where((source.shortsignal & source.newtradedirection | source.shortsignal) & TrailStop, source.ShortTrailSL, np.nan)

source['longsignal'] = np.where(source.longsignal, source.Close - source.Close * 3 / 100, np.nan)
source['shortsignal'] = np.where(source.shortsignal, source.Close + source.Close * 3 / 100, np.nan)

# ////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////   PLOTS   ///////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(source.index, source.Close)

# ////////////////// Signals //////////////////

plt.scatter(x = source.index, y = source.longsignal, marker = '^', color = '#3064fc', label = 'Long Signal')
plt.scatter(x = source.index, y = source.shortsignal, marker = 'v', color = '#fc1049', label = 'Short Signal')

# ////////////////// Stop Losses //////////////////

# // MAE Stop
    
# plot(SLenable and not TrailStop and longsignal  and (newtradedirection or strategy.position_size == 0) ? SLlongsaved  : na,
#  title="Long MAE Stop Start" , color=color.red, style=plot.style_linebr, linewidth=6)
# plot(SLenable and not TrailStop and shortsignal and (newtradedirection or strategy.position_size == 0) ? SLshortsaved : na,
#  title="Short MAE Stop Start", color=color.red, style=plot.style_linebr, linewidth=6)
# plot(SLenable and not TrailStop and strategy.position_size == 1  ? SLlongsaved  : na,
#  title="Long MAE Stop" , color=color.red, style=plot.style_linebr)
# plot(SLenable and not TrailStop and strategy.position_size == -1 ? SLshortsaved : na,
#  title="Short MAE Stop", color=color.red, style=plot.style_linebr)

# // Trailing Stop
    
# plot(TrailStop and longsignal  and (newtradedirection or strategy.position_size == 0) ? TrailSLlongsaved  : na,
#  title="Long Trailing Start" , color=color.orange, style=plot.style_linebr, linewidth=6)
# plot(TrailStop and shortsignal and (newtradedirection or strategy.position_size == 0) ? TrailSLshortsaved : na,
#  title="Short Trailing Start", color=color.orange, style=plot.style_linebr, linewidth=6)
# plot(TrailStop ? TrailSLlongsaved  : na, title="Long Trailing Stop" , color= strategy.position_size ==  1 and TrailSLlongsaved  < LongEntryPrice  ?
#  color.red : strategy.position_size == 1  and TrailSLlongsaved  > LongEntryPrice  ? color.green : color.rgb(0,0,0,100))
# plot(TrailStop ? TrailSLshortsaved : na, title="Short Trailing Stop", color= strategy.position_size == -1 and TrailSLshortsaved > ShortEntryPrice ?
#  color.red : strategy.position_size == -1 and TrailSLshortsaved < ShortEntryPrice ? color.green : color.rgb(0,0,0,100))

# ////////////////// Bollinger Bands //////////////////

# fill(PriceUpperLine, PriceLowerLine, title="BBprice Fill", color = 
#  volExtrmHigh and BBvol > BBvol[1] ? color.new(#ff1010, transp=70) : 
#  volExtrmHigh and BBvol < BBvol[1] ? color.new(#ff1010, transp=75) : 
#  volExtrmLow  and BBvol < BBvol[1] ? color.new(#10ff10, transp=70) : 
#  volExtrmLow  and BBvol > BBvol[1] ? color.new(#10ff10, transp=75) : 
#  color.new(color.white, transp=90))
# colors = ['#ff1010' if (source['volExtrmHigh'] & (source['BBvol'] > source['BBvol'].shift(1)))
#             elif '#ff1010' source['volExtrmHigh'] & (source['BBvol'] < source['BBvol'].shift(1)):
#         color = 
#     elif source['volExtrmLow'] & (source['BBvol'] < source['BBvol'].shift(1)):
#         color = '#10ff10'
#     elif source['volExtrmLow'] & (source['BBvol'] > source['BBvol'].shift(1)):
#         color = '#10ff10'
#     else:
#         color = 'gray']

plt.plot(source.EMA, color = 'black', label = 'Moving Average')
plt.plot(source.BBupper, label = 'Upper Bound', color = 'gray')
plt.plot(source.BBlower, label = 'Lower Bound', color = 'gray')
plt.fill_between(source.index, source.BBupper, source.BBlower, color = 'gray', alpha = 0.3, interpolate = True)

# ////////////////// Volatility //////////////////

plt.plot(source.BBvol, label = 'BBvol', color = 'blue')
plt.plot(source.SignalLine, label = 'Signal Line', color = 'fuchsia')
plt.plot(source.BaseLine, label = 'Base Line', color = 'yellow')
plt.plot(source.HighVolLvl, label = 'BBvol Upper', color = 'yellow')
plt.plot(source.LowVolLvl, label = 'BBvol Lower', color = 'yellow')
plt.fill_between(source.index, source.HighVolLvl, source.LowVolLvl, color = 'yellow', alpha = 0.3)

# ////////////////// Date and/or Time exclusion //////////////////

# bgcolor(DateFilter and UseDateFilter ? color.rgb(255,70,70,85) : na, title="Date Filter")
# bgcolor(TimeFilter and UseTimeFilter ? color.rgb(255,70,70,85) : na, title="Time Filter")

plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()

# ////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////   STRATEGY ENTRY/EXIT   ////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////

# ////////////////// Longs

# if longsignalonly and newtradedirection
#     strategy.entry(id="Long"           ,long=true)
# strategy.exit     (id="Long exit1"     ,from_entry="Long",
#  stop  = SLenable and not TrailStop ? SLlongsaved  : TrailStop ? TrailSLlongsaved  : newtradedirection ? BBupper : na,  
#  when  = strategy.position_size > 0)

# if longsignalonly and strategy.position_size == 0 and REenter
#     strategy.entry(id="Long after SL"  ,long=true)
# strategy.exit     (id="Long exit2"     ,from_entry="Long after SL",
#  stop  = SLenable and not TrailStop ? SLlongsaved  : TrailStop ? TrailSLlongsaved  : newtradedirection ? BBupper : na, 
#  when  = strategy.position_size > 0)

# ////////////////// Shorts

# if shortsignalonly and newtradedirection
#     strategy.entry(id="Short"          ,long=false)
# strategy.exit     (id="Short exit1"    ,from_entry="Short",
#  stop  = SLenable and not TrailStop ? SLshortsaved : TrailStop ? TrailSLshortsaved : newtradedirection ? BBlower : na,
#  when  = strategy.position_size < 0)

# if shortsignalonly and strategy.position_size == 0 and REenter
#     strategy.entry(id="Short after SL" ,long=false)
# strategy.exit     (id="Short exit2"    ,from_entry="Short after SL",
#  stop  = SLenable and not TrailStop ? SLshortsaved : TrailStop ? TrailSLshortsaved : newtradedirection ? BBlower : na,
#  when  = strategy.position_size < 0)