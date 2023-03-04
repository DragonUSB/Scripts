import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

df = pd.read_csv('ETHUSDT_1d.csv', sep = ",")
df['Close_Timestamp'] = pd.to_datetime(df['Close_Timestamp'], format='%Y-%m-%d')
df = df[['Close_Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']].copy()
df = df[df['Volume'] != 0]
df.reset_index(drop = True, inplace = True)

df = df.iloc[int(len(df) / 2):]

class SmaCross(Strategy):
    n1 = 7
    n2 = 14

    def init(self):
        super().init()
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        super().next() 
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

bt = Backtest(df, SmaCross, cash = 10000, commission = .002, exclusive_orders = True)

output = bt.run()
print(output)
bt.plot()