import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, plot, iplot, init_notebook_mode
import mplfinance as mpf
import matplotlib.pyplot as plt
from colorama import init, Back

plt.style.use('seaborn-v0_8-whitegrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

#%matplotlib inline

datos = pd.read_csv('Scripts/Python Scripts/ETHUSDT_1d.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)
datos.columns
datos.head()
datos.tail()
datos.dtypes
# datos.Close.plot(kind = 'line')

def EMA(df, n):
    EMA = df.ewm(span = n, min_periods = n - 1, adjust = False).mean()
    return EMA.dropna()

datos['ema5'] = EMA(datos.Close, 5)
# datos['ema5'].plot()
datos['ema10'] = EMA(datos.Close, 10)
# datos['ema10'].plot()

datos.head(30)

columnas = ['Close', 'ema5', 'ema10']

# fig = go.Figure()
# for column in columnas:
#     fig.add_trace(go.Scatter(x = datos.index, y = datos[column]))
# fig.show()

datos['alpha'] = datos['ema5'] - datos['ema10']
# datos['alpha'].plot()

datos['alpha_bin'] = datos['alpha'].apply(np.sign)
# datos['alpha_bin'].plot()
datos['alpha_bin'].value_counts()

datos['alpha_trade_long'] = ((datos['alpha_bin'] == 1) & (datos['alpha_bin'].shift(1) == -1) & (datos['alpha_bin'].shift(2) == -1) & (datos['alpha_bin'].shift(3) == -1))
datos['alpha_trade_short'] = ((datos['alpha_bin'] == -1) & (datos['alpha_bin'].shift(1) == 1) & (datos['alpha_bin'].shift(2) == 1) & (datos['alpha_bin'].shift(3) == 1))

datos['alpha_trade_long'].value_counts()
datos['alpha_trade_short'].value_counts()

datos['alpha_trade_compra'] = np.where(datos['alpha_trade_long'] == True, datos['ema5'], np.nan)
datos['alpha_trade_venta'] = np.where(datos['alpha_trade_short'] == True, datos['ema5'], np.nan)

datos.loc[datos['alpha_trade_long'], 'side'] = 1
datos.loc[datos['alpha_trade_short'], 'side'] = -1

print(datos.side.value_counts())

datos['side'] = datos['side'].shift(1)

datos['Returns'] = np.log(datos['Close']).diff()

datos['Position_Sum'] = datos['side'].fillna(0).cumsum()
# datos['Position_Sum'].plot()

columnas = ['ema5', 'ema10', 'alpha_trade_compra', 'alpha_trade_venta']

for column in columnas:
    
    if column == 'alpha_trade_compra':
        datos.plot(x = 'Open_Timestamp', y = 'alpha_trade_compra', kind = 'scatter', c = 'green', rot = 45)
    
    elif column == 'alpha_trade_venta':
        datos.plot(x = 'Open_Timestamp', y = 'alpha_trade_venta', kind = 'scatter', c = 'red', rot = 45)
        
    else:
        datos.plot(y = column, kind = 'line', rot = 45)
        
# Grafico con mplfinance
ap0 = [ mpf.make_addplot(datos['ema5'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(datos['ema10'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(datos, type = 'candle', volume = True, style = 'binance', addplot = ap0)

# Grafico con mplfinance acotando los dias
datos1 = datos.iloc[-120:-1,:]
ap1 = [ mpf.make_addplot(datos1['ema5'], color = 'g'),  # uses panel 0 by default
        mpf.make_addplot(datos1['ema10'], color = 'b'),  # uses panel 0 by default
      ]
mpf.plot(datos1, type = 'candle', volume = True, style = 'binance', addplot = ap1)

# Seleccionar un periodo de prueba
df_test = datos.iloc[-int(len(datos) / 2):,:].copy()
df_test['Cum_prod'] = (1 + df_test['Returns']).cumprod()
df_test['side'] = df_test['side'].fillna(0)

# Crear nuevo plot con senales
df_test['Buy_Signal'] = df_test.apply(lambda x: x.Close if x.side == 1 else np.nan, axis = 1)
df_test['Sell_Signal'] = df_test.apply(lambda x: x.Close if x.side == -1 else np.nan, axis = 1)

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(df_test.index, df_test.Close)
plt.plot(df_test.index, df_test.ema5)
plt.plot(df_test.index, df_test.ema10)
plt.scatter(x = df_test.index, y = df_test["Buy_Signal"], marker = '^')
plt.scatter(x = df_test.index, y = df_test["Sell_Signal"], marker = 'v')
plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()

# Valores iniciales de la estrategia
backtest = []
f_tick = 'UNI'
tick = 'USDT'
initial_cash_inv = 10
initial_cash = initial_cash_inv
initial_position = 0
initial_holdings = 0
initial_total = initial_cash + initial_holdings

for idx, row in df_test.iterrows():
    # Regla de lado
    precio = row['Close']
    dia = idx
    if row['side'] == 0:
        backtest.append([dia, initial_cash, initial_position, precio, initial_holdings, initial_total])
        continue
    
    elif ((row['side'] == 1) & (initial_cash >= 10)):
        f_unidades = round(initial_cash / precio, 8)
        print(Back.GREEN + '..................................................')
        print(Back.GREEN + f'{idx}')
        print(Back.GREEN + f'Comprando {f_unidades} de {f_tick} a {precio} {tick}')
        initial_cash = initial_cash - (precio * f_unidades)
        print(Back.GREEN + 'Actualizando Cash')
        print(Back.GREEN + f'Cash disponible: {initial_cash}')
        initial_position = initial_position + f_unidades
        print(Back.GREEN + f'Posicion actual: {initial_position}')
        # Reglas de cash
        precio_compra = precio
        initial_holdings = precio * initial_position
        initial_total = initial_cash + initial_holdings
        backtest.append([dia, initial_cash, initial_position, precio, initial_holdings, initial_total])
        
    elif row['side'] == -1:
        
        if initial_position == 0 or precio < precio_compra:
            print('..................................................')
            print('Sin posicion')
            backtest.append([dia, initial_cash, initial_position, precio, initial_holdings, initial_total])
            continue
        
        print(Back.RED + '..................................................')
        print(Back.RED + f'{idx}')
        print(Back.RED + f'Vendiendo {f_unidades} de {f_tick} a {precio} {tick}')
        initial_cash = initial_cash + (precio * f_unidades)
        print(Back.RED + 'Actualizando Cash')
        print(Back.RED + f'Cash disponible: {initial_cash}')
        initial_position = initial_position - f_unidades
        print(Back.RED + f'Posicion actual: {initial_position}')
        # Reglas de cash
        initial_holdings = precio * initial_position
        initial_total = initial_cash + initial_holdings
        backtest.append([dia, initial_cash, initial_position, precio, initial_holdings, initial_total])
        
back_test = pd.DataFrame(backtest)
back_test.columns = ['Dia', 'Cash_USDT', 'Posiciones', 'Precio Cierre', 'Valor Posiciones', 'Cash + Valor Pos']
back_test['Dia'] = pd.to_datetime(back_test['Dia'], format='%Y-%m-%d')
back_test.set_index('Dia', inplace = True)

print('..................................................')
print('Estrategia Desde el ' + str(df_test.index[0]) + ' Hasta el ' + str(df_test.index[-1]))
print(f'Cantidad de {f_tick} disponibles: ' + str(back_test['Posiciones'].iloc[-1]))
print(f'Cash disponible en {tick}: ' + str(back_test['Cash_USDT'].iloc[-1]))

retorno = ((back_test['Cash_USDT'].iloc[-1] - initial_cash_inv) * 100) / initial_cash_inv
print('..................................................')
print(f'Retorno de la estrategia {retorno}%')

retorno_buy_hold = (df_test['Close'].iloc[-1] / df_test['Close'].iloc[1]) * 100
print('..................................................')
print(f'Retorno de la estrategia Buy Hold {retorno_buy_hold}%')
print('..................................................')

# Grafico con matplotlib
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Medias Moviles Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos.ema5)
plt.plot(datos.index, datos.ema10)
plt.scatter(x = df_test.index, y = df_test["Buy_Signal"], marker = '^')
plt.scatter(x = df_test.index, y = df_test["Sell_Signal"], marker = 'v')
plt.setp(ax1.get_xticklabels(), visible = False)
ax2 = plt.subplot(312, sharex = ax1)
plt.plot(datos.index, datos['Position_Sum'])
plt.plot(df_test.index, df_test['Cum_prod'])
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(313, sharex = ax1)
plt.plot(back_test.index, back_test.Cash_USDT)
plt.grid(True)
plt.show()

# Grafico con matplotlib acotando los dias
datos1 = datos.iloc[-int(len(datos) / 2):,:]
df_test1 = df_test.iloc[-int(len(datos) / 2):,:]
back_test1 = back_test.iloc[-int(len(datos) / 2):,:]
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Medias Moviles Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos1.index, datos1.Close)
plt.plot(datos1.index, datos1.ema5)
plt.plot(datos1.index, datos1.ema10)
plt.scatter(x = df_test1.index, y = df_test1["Buy_Signal"], marker = '^')
plt.scatter(x = df_test1.index, y = df_test1["Sell_Signal"], marker = 'v')
plt.setp(ax1.get_xticklabels(), visible = False)
ax2 = plt.subplot(312, sharex = ax1)
plt.plot(datos1.index, datos1['Position_Sum'])
plt.plot(df_test1.index, df_test1['Cum_prod'])
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(313, sharex = ax1)
plt.plot(back_test1.index, back_test1.Cash_USDT)
plt.grid(True)
plt.show()