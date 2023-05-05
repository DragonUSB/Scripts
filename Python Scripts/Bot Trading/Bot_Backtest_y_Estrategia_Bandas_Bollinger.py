import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Back

plt.style.use('seaborn-v0_8-whitegrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

f_tick = input('Coloque la criptomeneda que se va analizar: ')
tick = 'USDT'

df_raw = pd.read_csv('Scripts/Python Scripts/' + f_tick + tick + '_1d.csv')

# Limpiando y dar formato
df = df_raw[['Close_Timestamp', 'Close']].copy()
df['Close_Timestamp'] = pd.to_datetime(df['Close_Timestamp'], format='%Y-%m-%d')
df.set_index('Close_Timestamp', inplace = True)
# df.plot()

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

# Calcular a 26 dias
datos = b_bands(df, 15)
# datos.plot()

# Ejemplo
# datos.iloc[-100:,:].plot()

# Crear Senales
datos['side'] = np.nan

long_signals = (datos['Close'] <= datos['Bb_15'])
short_signals = (datos['Close'] >= datos['BB_15'])

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

fig = plt.figure(figsize = (12, 6))
ax1 = plt.subplot()
plt.plot(df_test.index, df_test.Close)
plt.plot(df_test.index, df_test.Bb_15)
plt.plot(df_test.index, df_test.BB_15)
plt.scatter(x = df_test.index, y = df_test["Buy_Signal"], marker = '^')
plt.scatter(x = df_test.index, y = df_test["Sell_Signal"], marker = 'v')
plt.legend()
plt.grid(True)
plt.title('UNIUSDT Estrategia')
plt.show()

# Valores iniciales de la estrategia
backtest = []
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
fig.suptitle(f'Band Bollinger Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos.Bb_15)
plt.plot(datos.index, datos.BB_15)
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
fig.suptitle(f'Band Bollinger Strategy para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(311)
plt.plot(datos1.index, datos1.Close)
plt.plot(datos1.index, datos1.Bb_15)
plt.plot(datos1.index, datos1.BB_15)
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