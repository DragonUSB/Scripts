import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

datos = pd.read_csv('UNIUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)

datos['Number'] = np.arange(len(datos)) + 1
datos_high = datos.copy()
datos_low = datos.copy()
print(datos.tail())

# higher points are returned
while len(datos_high) > 2:
    slope, intercept, r_value, p_value, std_err = linregress(x = datos_high['Number'], y = datos_high['High'])
    datos_high = datos_high.loc[datos_high['High'] > slope * datos_high['Number'] + intercept]
    
print(datos_high.tail())

# lower points are returned
while len(datos_low) >  2:
    slope, intercept, r_value, p_value, std_err = linregress(x = datos_low['Number'], y = datos_low['Low'])
    datos_low = datos_low.loc[datos_low['Low'] < slope * datos_low['Number'] + intercept]
    
print(datos_low.tail())

slope, intercept, r_value, p_value, std_err = linregress(x = datos_high['Number'], y = datos_high['Close'])
datos['Uptrend'] = slope * datos['Number'] + intercept

slope, intercept, r_value, p_value, std_err = linregress(x = datos_low['Number'], y = datos_low['Close'])
datos['Downtrend'] = slope * datos['Number'] + intercept

print(datos.tail())

# draw the closing price and related trendlines (uptrend and downtrend)
fig, ax1 = plt.subplots(figsize = (12, 6))

color = 'tab:green'
xdate = [x.date() for x in datos.index]
ax1.set_xlabel('Date', color = color)
ax1.plot(xdate, datos.Close, label = "close", color = color)
ax1.tick_params(axis = 'x', labelcolor = color)
ax1.legend()

ax2 = ax1.twiny() # ax2 and ax1 will have common y axis and different x axis, twiny
ax2.plot(datos.Number, datos.Uptrend, label = "uptrend")
ax2.plot(datos.Number, datos.Downtrend, label = "downtrend")

plt.legend()
plt.grid()
plt.show()