import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl

quandl.ApiConfig.api_key = "MGz7SvL7fiWyqe_j8QKM"
datos1 = quandl.get("BCHAIN/MIREV")
datos1 = datos1.rename(columns={'Value': 'MIREV'})
datos2 = quandl.get("BCHAIN/HRATE")
datos2 = datos2.rename(columns={'Value': 'HRATE'})
datos3 = pd.read_csv('BTCUSDT_1d.csv', sep = ",")
datos3['Open_Timestamp'] = pd.to_datetime(datos3['Open_Timestamp'], format='%Y-%m-%d')
datos3 = datos3[['Open_Timestamp', 'Close']].copy()
datos3 = datos3.rename(columns={'Open_Timestamp': 'Date'})
datos3.set_index('Date', inplace = True)
datos3 = datos3.join(datos1)
datos3 = datos3.join(datos2)

# Media Movil Simple
def MA(df, n):
    MA = pd.Series(pd.Series.rolling(df['MIREV'], n).mean(), name = 'MA_' + str(n))
    df = df.join(MA)
    return df

datos3 = MA(datos3, 365)

# Puell_Multiple = Mining Revenue / SMA(Mining Revenue, 365)
datos3['Puell_Multiple'] = datos3['MIREV'] / datos3['MA_365']

# PetaHashDollar = Mining Revenue / Hash Rate
datos3['PetaHashDollar'] = datos3['MIREV'] / datos3['HRATE']

# PLOT
fig1, ax1 = plt.subplots(figsize = (12, 6))
ax1.plot(datos3.index, datos3.Close, color = 'r')
ax1.tick_params(axis='y', labelcolor = 'r')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(datos3.index, datos3.Puell_Multiple, color = 'b')
ax2.set_ylim(0, 10)
ax2.tick_params(axis='y', labelcolor = 'b')
fig1.tight_layout()
plt.show()

fig2, ax1 = plt.subplots(figsize = (12, 6))
ax1.plot(datos3.index, datos3.Close, color = 'r')
ax1.tick_params(axis='y', labelcolor = 'r')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.plot(datos3.index, datos3.PetaHashDollar, color = 'b')
ax2.set_ylim(0, 10)
ax2.tick_params(axis='y', labelcolor = 'b')
fig2.tight_layout()
plt.show()