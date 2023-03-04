import pandas as pd
import numpy as np
from backtesting import Strategy
from backtesting import Backtest

df_raw = pd.read_csv('ETHUSDT_1d.csv')
df = df_raw[['Close_Timestamp', 'Open', 'High', 'Low', 'Close']].copy()
df['Close_Timestamp'] = pd.to_datetime(df['Close_Timestamp'], format='%Y-%m-%d')
df.set_index('Close_Timestamp', inplace = True)

# Calcular Metricas (Bandas de Bollinger)
def b_bands(df, n):
    MA = pd.Series(pd.Series.rolling(df['Close'], n).mean())
    MSD = pd.Series(pd.Series.rolling(df['Close'], n).std())
    b1 = MA + (MSD*2)
    B1 = pd.Series(b1, name = 'BB_' + str(n))
    df = df.join(B1)
    b2 = MA - (MSD*2)
    B2 = pd.Series(b2, name = 'Bb_' + str(n))
    df = df.join(B2)
    return df

# Calcular Bandas
datos = b_bands(df, 15)

# Crear Senales
datos['side'] = np.nan

long_signals = (datos['Close'] <= datos['Bb_15'])
short_signals = (datos['Close'] >= datos['BB_15'])

datos.loc[long_signals, 'side'] = 1
datos.loc[short_signals, 'side'] = -1

# Revisar carga de la estrategia
print(datos.side.value_counts())

datos=datos.iloc[int(len(datos) / 2):]

def SIGNAL():
    return datos.side

class MyCandlesStrat(Strategy):  
    def init(self):
        super().init()
        self.signal1 = self.I(SIGNAL)

    def next(self):
        super().next() 
        if self.signal1 == 1:
            sl1 = self.data.Close[-1] - self.data.Close[-1] * 0.01
            tp1 = self.data.Close[-1] + self.data.Close[-1] * 0.5
            self.buy(sl = sl1, tp = tp1)
        elif self.signal1 == -1:
            sl1 = self.data.Close[-1] + self.data.Close[-1] * 0.01
            tp1 = self.data.Close[-1] - self.data.Close[-1] * 0.5
            self.sell(sl=sl1, tp = tp1)

bt = Backtest(datos, MyCandlesStrat, cash = 10_000, commission = .002, exclusive_orders = True)
stat = bt.run()
print(stat)

bt.plot()