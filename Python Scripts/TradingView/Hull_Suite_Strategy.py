import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Back

plt.style.use('seaborn-darkgrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

datos = pd.read_csv('ETHUSDT_1h.csv', sep=",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos.set_index('Close_Timestamp', inplace = True)

# Weighted Moving Average
def WMA(df, n):
    weights = np.arange(1, n + 1)
    WMA = pd.Series(pd.Series.rolling(df['Close'], n).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw = True), name = 'WMA_' + str(n))
    df = df.join(WMA)
    return df

# Hull Moving Average
def HMA(df, n):
    df1 = pd.DataFrame({'Close': []})
    WMA1 = WMA(df, n)
    WMA1str = 'WMA_' + str(n)
    WMA2 = WMA(WMA1, n // 2)
    WMA2str = 'WMA_' + str(n // 2)
    sqrtn = pow(n, 0.5)
    df1['Close'] = 2 * WMA2[WMA2str] - WMA2[WMA1str]
    HMA = WMA(df1, int(sqrtn))
    HMA2str = 'WMA_' + str(int(sqrtn))
    HMA = pd.Series(HMA[HMA2str], name = 'HMA_' + str(n))
    df = df.join(HMA)
    return df

datos = HMA(datos, 55)
datos['MHULL'] = datos['HMA_55'].shift(0)
datos['SHULL'] = datos['HMA_55'].shift(2)

datos['longsignal'] = np.where((datos['MHULL'] > datos['SHULL']) & (datos['MHULL'].shift(1) < datos['SHULL'].shift(1)), datos.Close - datos.Close * 3 / 100, np.nan)
datos['shortsignal'] = np.where((datos['MHULL'] < datos['SHULL']) & (datos['MHULL'].shift(1) > datos['SHULL'].shift(1)), datos.Close + datos.Close * 3 / 100, np.nan)

datos = HMA(datos, 200)

# Plot
fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos.MHULL, label = 'MHULL', color = 'green')
plt.plot(datos.index, datos.SHULL, label = 'SHULL', color = 'red')
plt.plot(datos.index, datos.HMA_200, label = 'HMA 200', color = 'blue')
plt.fill_between(datos.index, datos.MHULL, datos.SHULL, where=datos.MHULL >= datos.SHULL, color='green')
plt.fill_between(datos.index, datos.MHULL, datos.SHULL, where=datos.MHULL < datos.SHULL, color='red')
plt.scatter(x = datos.index, y = datos.longsignal, marker = '^', color = '#3064fc', label = 'Long Signal')
plt.scatter(x = datos.index, y = datos.shortsignal, marker = 'v', color = '#fc1049', label = 'Short Signal')
plt.legend()
plt.grid(True)
plt.title('Hull Suite Strategy')
plt.show()

# Crear Senales
datos['side'] = np.nan

long_signals = (datos['MHULL'] > datos['SHULL']) & (datos['MHULL'].shift(1) < datos['SHULL'].shift(1))
short_signals = (datos['MHULL'] < datos['SHULL']) & (datos['MHULL'].shift(1) > datos['SHULL'].shift(1))

datos.loc[long_signals, 'side'] = 1
datos.loc[short_signals, 'side'] = -1

# Revisar carga de la estrategia
print(datos.side.value_counts())

# Agregar Lag a nuestra serie
datos['side'] = datos['side'].shift(1)

# calcular retornos
datos['Returns'] = np.log(datos['Close']).diff()

# Calcular posiciones teoricas
datos['Position_Sum'] = datos['side'].fillna(0).cumsum()

# Seleccionar un periodo de prueba
df_test = datos.iloc[-int(len(datos) / 2):,:].copy()
df_test['Cum_prod'] = (1 + df_test['Returns']).cumprod()
df_test['side'] = df_test['side'].fillna(0)

# Crear nuevo plot con senales
df_test['Buy_Signal'] = df_test.apply(lambda x: x.Close if x.side == 1 else np.nan, axis = 1)
df_test['Sell_Signal'] = df_test.apply(lambda x: x.Close if x.side == -1 else np.nan, axis = 1)

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
        initial_cash = round(initial_cash, 8)
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
        initial_cash = round(initial_cash, 8)
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
retorno = round(retorno, 2)
print('..................................................')
print(f'Retorno de la estrategia {retorno}%')

retorno_buy_hold = (df_test['Close'].iloc[-1] / df_test['Close'].iloc[1]) * 100
retorno_buy_hold = round(retorno_buy_hold, 2)
print('..................................................')
print(f'Retorno de la estrategia Buy Hold {retorno_buy_hold}%')
print('..................................................')

# Grafico con matplotlib
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Hull Suite Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos.MHULL, label = 'MHULL', color = 'green')
plt.plot(datos.index, datos.SHULL, label = 'SHULL', color = 'red')
plt.fill_between(datos.index, datos.MHULL, datos.SHULL, where=datos.MHULL >= datos.SHULL, color='green')
plt.fill_between(datos.index, datos.MHULL, datos.SHULL, where=datos.MHULL < datos.SHULL, color='red')
plt.scatter(x = datos.index, y = datos.longsignal, marker = '^', color = '#3064fc', label = 'Long Signal')
plt.scatter(x = datos.index, y = datos.shortsignal, marker = 'v', color = '#fc1049', label = 'Short Signal')
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
fig.suptitle(f'Hull Suite Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos1.index, datos1.Close)
plt.plot(datos1.index, datos1.MHULL, label = 'MHULL', color = 'green')
plt.plot(datos1.index, datos1.SHULL, label = 'SHULL', color = 'red')
plt.fill_between(datos1.index, datos1.MHULL, datos1.SHULL, where=datos1.MHULL >= datos1.SHULL, color='green')
plt.fill_between(datos1.index, datos1.MHULL, datos1.SHULL, where=datos1.MHULL < datos1.SHULL, color='red')
plt.scatter(x = datos1.index, y = datos1.longsignal, marker = '^', color = '#3064fc', label = 'Long Signal')
plt.scatter(x = datos1.index, y = datos1.shortsignal, marker = 'v', color = '#fc1049', label = 'Short Signal')
plt.setp(ax1.get_xticklabels(), visible = False)
ax2 = plt.subplot(312, sharex = ax1)
plt.plot(datos1.index, datos1['Position_Sum'])
plt.plot(df_test1.index, df_test1['Cum_prod'])
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(313, sharex = ax1)
plt.plot(back_test1.index, back_test1.Cash_USDT)
plt.grid(True)
plt.show()