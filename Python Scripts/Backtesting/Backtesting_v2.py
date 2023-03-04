import pandas as pd
import numpy as np
from backtesting import Strategy
from backtesting import Backtest

df = pd.read_csv('ETHUSDT_1d.csv', sep = ",")
df['Close_Timestamp'] = pd.to_datetime(df['Close_Timestamp'], format='%Y-%m-%d')
df = df[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
df = df[df['Volume'] != 0]
df.reset_index(drop = True, inplace = True)

def support(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l - n1 + 1, l + 1):
        if(df1.Low[i] > df1.Low[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if(df1.Low[i] < df1.Low[i - 1]):
            return 0
    return 1

def resistance(df1, l, n1, n2): #n1 n2 before and after candle l
    for i in range(l - n1 + 1, l + 1):
        if(df1.High[i] < df1.High[i - 1]):
            return 0
    for i in range(l + 1, l + n2 + 1):
        if(df1.High[i] > df1.High[i - 1]):
            return 0
    return 1

length = len(df)
High = list(df['High'])
Low = list(df['Low'])
Close = list(df['Close'])
Open = list(df['Open'])
bodydiff = [0] * length

Highdiff = [0] * length
Lowdiff = [0] * length
ratio1 = [0] * length
ratio2 = [0] * length

def isEngulfing(l):
    row = l
    bodydiff[row] = abs(Open[row] - Close[row])
    if bodydiff[row] < 0.000001:
        bodydiff[row] = 0.000001      

    bodydiffmin = 0.002
    if (bodydiff[row] > bodydiffmin and bodydiff[row - 1] > bodydiffmin and
        Open[row - 1] < Close[row - 1] and
        Open[row] > Close[row] and 
        (Open[row] - Close[row - 1]) >= -0e-5 and Close[row] < Open[row - 1]): #+0e-5 -5e-5
        return 1

    elif(bodydiff[row] > bodydiffmin and bodydiff[row - 1] > bodydiffmin and
        Open[row - 1] > Close[row - 1] and
        Open[row] < Close[row] and 
        (Open[row] - Close[row - 1]) <= +0e-5 and Close[row] > Open[row - 1]):#-0e-5 +5e-5
        return 2
    else:
        return 0
       
def isStar(l):
    bodydiffmin = 0.0020
    row = l
    Highdiff[row] = High[row] - max(Open[row], Close[row])
    Lowdiff[row] = min(Open[row], Close[row]) - Low[row]
    bodydiff[row] = abs(Open[row] - Close[row])
    if bodydiff[row] < 0.000001:
        bodydiff[row] = 0.000001
    ratio1[row] = Highdiff[row] / bodydiff[row]
    ratio2[row] = Lowdiff[row] / bodydiff[row]

    if (ratio1[row] > 1 and Lowdiff[row] < 0.2 * Highdiff[row] and bodydiff[row] > bodydiffmin):# and Open[row]>Close[row]):
        return 1
    elif (ratio2[row] > 1 and Highdiff[row] < 0.2 * Lowdiff[row] and bodydiff[row] > bodydiffmin):# and Open[row]<Close[row]):
        return 2
    else:
        return 0
    
def CloseResistance(l, levels, lim):
    if len(levels) == 0:
        return 0
    c1 = abs(df.High[l] - min(levels, key = lambda x: abs(x - df.High[l]))) <= lim
    c2 = abs(max(df.Open[l], df.Close[l]) - min(levels, key = lambda x: abs(x - df.High[l]))) <= lim
    c3 = min(df.Open[l], df.Close[l]) < min(levels, key = lambda x: abs(x - df.High[l]))
    c4 = df.Low[l] < min(levels, key = lambda x: abs(x - df.High[l]))
    if( (c1 or c2) and c3 and c4 ):
        return 1
    else:
        return 0
    
def CloseSupport(l, levels, lim):
    if len(levels) == 0:
        return 0
    c1 = abs(df.Low[l] - min(levels, key = lambda x: abs(x - df.Low[l]))) <= lim
    c2 = abs(min(df.Open[l], df.Close[l]) - min(levels, key = lambda x: abs(x - df.Low[l]))) <= lim
    c3 = max(df.Open[l], df.Close[l]) > min(levels, key = lambda x: abs(x - df.Low[l]))
    c4 = df.High[l] > min(levels, key = lambda x: abs(x - df.Low[l]))
    if( (c1 or c2) and c3 and c4 ):
        return 1
    else:
        return 0

n1 = 2
n2 = 2
backCandles = 30
signal = [0] * length

for row in range(backCandles, len(df) - n2):
    ss = []
    rr = []
    for subrow in range(row - backCandles + n1, row + 1):
        if support(df, subrow, n1, n2):
            ss.append(df.Low[subrow])
        if resistance(df, subrow, n1, n2):
            rr.append(df.High[subrow])
    #!!!! parameters
    if ((isEngulfing(row) == 1 or isStar(row) == 1) and CloseResistance(row, rr, 150e-5) ):#and df.RSI[row]<30
        signal[row] = 1
    elif((isEngulfing(row) == 2 or isStar(row) == 2) and CloseSupport(row, ss, 150e-5)):#and df.RSI[row]>70
        signal[row] = 2
    else:
        signal[row] = 0

df['signal'] = signal

# print(df[df['signal']==1].count())
# print(df[df['signal']==2].count())

df.columns = ['Local time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Signal']
df=df.iloc[int(len(df) / 2):]

def SIGNAL():
    return df.Signal

class MyCandlesStrat(Strategy):  
    def init(self):
        super().init()
        self.signal1 = self.I(SIGNAL)

    def next(self):
        super().next() 
        if self.signal1 == 2:
            sl1 = self.data.Close[-1] - self.data.Close[-1] * 0.01
            tp1 = self.data.Close[-1] + self.data.Close[-1] * 0.5
            self.buy(sl = sl1, tp = tp1)
        elif self.signal1 == 1:
            sl1 = self.data.Close[-1] + self.data.Close[-1] * 0.01
            tp1 = self.data.Close[-1] - self.data.Close[-1] * 0.5
            self.sell(sl=sl1, tp = tp1)

bt = Backtest(df, MyCandlesStrat, cash = 10_000, commission = .002, exclusive_orders = True)
stat = bt.run()
print(stat)

bt.plot()