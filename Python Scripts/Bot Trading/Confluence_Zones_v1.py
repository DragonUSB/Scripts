import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from colorama import init, Back

plt.style.use('seaborn-darkgrid')

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

datos = pd.read_csv('ETHUSDT_1d.csv', sep = ",")
datos['Close_Timestamp'] = pd.to_datetime(datos['Close_Timestamp'], format='%Y-%m-%d')
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume']].copy()
datos.set_index('Close_Timestamp', inplace = True)
datos = datos.iloc[-1000:,:]

# Media Movil Exponencial
def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'], span = n, min_periods = n - 1, adjust = False).mean(), name = 'EMA_' + str(n))
    df = df.join(EMA)
    return df

# Moving Average Convergence Divergence
def MACD(df, f, s, sig, name):
    EMA1 = pd.Series(pd.Series.ewm(df['Close'], span = f, min_periods = f - 1, adjust = False).mean())
    EMA2 = pd.Series(pd.Series.ewm(df['Close'], span = s, min_periods = s - 1, adjust = False).mean())
    macd = EMA1 - EMA2
    MACD = pd.Series(macd, name = 'MACD_' + name)
    df = df.join(MACD)
    EMA3 = pd.Series(pd.Series.ewm(df['MACD_' + name], span = sig, min_periods = sig - 1, adjust = False).mean(), name = 'Signal_' + name)
    df = df.join(EMA3)
    hist = macd - EMA3
    HIST = pd.Series(hist, name = 'Histogram_' + name)
    df = df.join(HIST)
    return df

def rising(df, bars, histogram_name, name):
    ok = [False]
    for j in range(1,len(df[histogram_name])):
        current = df[histogram_name][j]
        if bars > 0 and bars <= len(df[histogram_name]):
            for i in range(1, bars + 1):
                if (not(np.isnan(df[histogram_name][j-i])) and current <= df[histogram_name][j-i]):
                    ok.append(False)
                else:
                    ok.append(True)
    ok = pd.Series(ok, index = df.index, name = 'rising_' + name)
    df = df.join(ok)
    return df

def falling(df, bars, histogram_name, name):
    ok = [False]
    for j in range(1,len(df[histogram_name])):
        current = df[histogram_name][j]
        if bars > 0 and bars <= len(df[histogram_name]):
            for i in range(1, bars + 1):
                if (not(np.isnan(df[histogram_name][j-i])) and current >= df[histogram_name][j-i]):
                    ok.append(False)
                else:
                    ok.append(True)
    ok = pd.Series(ok, index = df.index, name = 'falling_' + name)
    df = df.join(ok)
    return df

datos = EMA(datos, 12)
datos = EMA(datos, 26)
datos = EMA(datos, 84)
datos = EMA(datos, 182)
datos = EMA(datos, 10)
datos = EMA(datos, 55)
datos = EMA(datos, 588)
datos = EMA(datos, 1274)

# Confluence Zones
confluence_level = 2
datos = MACD(datos, 12, 26, 9, 'Line1')
datos = MACD(datos, (12 * 5), (26 * 5), (9 * 5), 'Line2')
datos = rising(datos, 1, 'Histogram_Line1', '1')
datos = rising(datos, 1, 'Histogram_Line2', '2')
datos = falling(datos, 1, 'Histogram_Line1', '1')
datos = falling(datos, 1, 'Histogram_Line2', '2')
is_bullish = datos['rising_1'] & datos['rising_2']
is_bearish = datos['falling_1'] & datos['falling_2']
histogram = datos['Histogram_Line1'] + datos['Histogram_Line2']

if confluence_level >= 3:
    datos = MACD(datos, (12 * 5 * 5), (26 * 5 * 5), (9 * 5 * 5), 'Line3')
    datos = rising(datos, 1, 'Histogram_Line3', '3')
    datos = falling(datos, 1, 'Histogram_Line3', '3')
    is_bullish = is_bullish & datos['rising_3']
    is_bearish = is_bearish & datos['falling_3']
    histogram = histogram + datos['Histogram_Line3']

if confluence_level == 4:
    datos = MACD(datos, (12 * 5 * 5 * 5), (26 * 5 * 5 * 5), (9 * 5 * 5 * 5), 'Line4')
    datos = rising(datos, 1, 'Histogram_Line4', '4')
    datos = falling(datos, 1, 'Histogram_Line4', '4')
    is_bullish = is_bullish & datos['rising_4']
    is_bearish = is_bearish & datos['falling_4']
    histogram = histogram + datos['Histogram_Line4']

is_bullish = pd.Series(is_bullish, index = datos.index, name = 'is_bullish')
datos = datos.join(is_bullish)
is_bearish = pd.Series(is_bearish, index = datos.index, name = 'is_bearish')
datos = datos.join(is_bearish)
histogram = pd.Series(histogram, index = datos.index, name = 'histogram')
datos = datos.join(histogram)

# Crear Senales
datos['side'] = np.nan

# long_signals = (datos['is_bullish'] == True) & (datos['is_bullish'].shift(1) == False)
# short_signals = (datos['is_bullish'] == True) & (datos['is_bullish'].shift(-1) == False)
histogram_bool = ((datos['histogram'].shift(-1) > datos['histogram']) & (datos['histogram'] >= 0)) | ((datos['histogram'].shift(-1) < datos['histogram']) & (datos['histogram'] <= 0))
long_signals = ((histogram_bool == True) & (histogram_bool.shift(1) == False) & (histogram_bool.shift(-1) == True) & (datos['histogram'] >= 0)) | (
                (histogram_bool == True) & (histogram_bool.shift(-1) == False) & (histogram_bool.shift(1) == True) & (datos['histogram'] <= 0))
short_signals = (datos['is_bullish'] == True) & (datos['is_bullish'].shift(-1) == False) & (histogram_bool == False)

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
df_test = datos.iloc[-1000:,:].copy()
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
        print(Back.GREEN + 'Actualizando Cash')
        print(Back.GREEN + f'Cash disponible: {initial_cash}')
        initial_position = initial_position + f_unidades
        print(Back.GREEN + f'Posicion actual: {initial_position}')
        # Reglas de cash
        initial_holdings = precio * initial_position
        initial_total = initial_cash + initial_holdings
        backtest.append([dia, initial_cash, initial_position, precio, initial_holdings, initial_total])
        
    elif row['side'] == -1:
        
        if initial_position == 0:
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

# Grafico con mplfinance
ap0 = [ mpf.make_addplot(datos['EMA_12'], color = '#000000', width = 1),
        mpf.make_addplot(datos['EMA_26'], color = '#ff9800', width = 2),
        mpf.make_addplot(datos['EMA_84'], color = '#078bf4', width = 2),
        mpf.make_addplot(datos['EMA_182'], color = '#e60202', width = 3),
        mpf.make_addplot(datos['EMA_10'], color = '#000000', width = 1),
        mpf.make_addplot(datos['EMA_55'], color = '#039709', width = 2)
      ]
mpf.plot(datos, type = 'candle', volume = True, style = 'binance', addplot = ap0,
         fill_between = dict(y1 = datos['Close'].values, y2 = datos['Low'].min(), where = datos['is_bullish'] | datos['is_bearish'], alpha = 0.5, color = ['g', 'r'])
        )

# Grafico con mplfinance acotando los dias
datos1 = datos.iloc[-180:,:]
ap1 = [ mpf.make_addplot(datos1['EMA_12'], color = '#000000', width = 1),
        mpf.make_addplot(datos1['EMA_26'], color = '#ff9800', width = 2),
        mpf.make_addplot(datos1['EMA_84'], color = '#078bf4', width = 2),
        mpf.make_addplot(datos1['EMA_182'], color = '#e60202', width = 3),
        mpf.make_addplot(datos1['EMA_10'], color = '#000000', width = 1),
        mpf.make_addplot(datos1['EMA_55'], color = '#039709', width = 2)
       ]
mpf.plot(datos1, type = 'candle', volume = True, style = 'binance', addplot = ap1,
         fill_between = dict(y1 = datos1['Close'].values, y2 = datos1['Low'].min(), where = datos1['is_bullish'] | datos1['is_bearish'], alpha = 0.5, color = ['g', 'r'])
        )

# Grafico con matplotlib
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Confluence Zones para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(411)
plt.plot(datos.index, datos.Close)
plt.plot(datos.index, datos['EMA_12'], color = '#000000', linewidth = 1)
plt.plot(datos.index, datos['EMA_26'], color = '#ff9800', linewidth = 2)
plt.plot(datos.index, datos['EMA_84'], color = '#078bf4', linewidth = 2)
plt.plot(datos.index, datos['EMA_182'], color = '#e60202', linewidth = 3)
plt.plot(datos.index, datos['EMA_10'], color = '#000000', linewidth = 1)
plt.plot(datos.index, datos['EMA_55'], color = '#039709', linewidth = 2)
plt.fill_between(datos.index, datos['Close'], datos['Low'].min(), where = datos['is_bullish'], alpha = 0.5, color = '#09f613')
plt.fill_between(datos.index, datos['Close'], datos['Low'].min(), where = datos['is_bearish'], alpha = 0.2, color = '#df0808')
plt.scatter(x = df_test.index, y = df_test["Buy_Signal"], marker = '^')
plt.scatter(x = df_test.index, y = df_test["Sell_Signal"], marker = 'v')
plt.setp(ax1.get_xticklabels(), visible = False)
ax2 = plt.subplot(412, sharex = ax1)
plt.plot(datos.index, datos['histogram'])
plt.fill_between(datos.index, datos['histogram'], y2 = 0, where = (datos['histogram'].shift(-1) > datos['histogram']) & (datos['histogram'] >= 0), color = '#10ed19', interpolate = True)
plt.fill_between(datos.index, datos['histogram'], y2 = 0, where = (datos['histogram'].shift(-1) < datos['histogram']) & (datos['histogram'] <= 0), color = '#db1c1c', interpolate = True)
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(413, sharex = ax1)
plt.plot(datos.index, datos['Position_Sum'])
plt.plot(df_test.index, df_test['Cum_prod'])
plt.setp(ax3.get_xticklabels(), visible = False)
ax4 = plt.subplot(414, sharex = ax1)
plt.plot(back_test.index, back_test.Cash_USDT)
plt.grid(True)
plt.show()

# Grafico con matplotlib acotando los dias
datos1 = datos.iloc[-180:,:]
df_test1 = df_test.iloc[-180:,:]
back_test1 = back_test.iloc[-180:,:]
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Confluence Zones para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0)
ax1 = plt.subplot(411)
plt.plot(datos1.index, datos1.Close)
plt.plot(datos1.index, datos1['EMA_12'], color = '#000000', linewidth = 1)
plt.plot(datos1.index, datos1['EMA_26'], color = '#ff9800', linewidth = 2)
plt.plot(datos1.index, datos1['EMA_84'], color = '#078bf4', linewidth = 2)
plt.plot(datos1.index, datos1['EMA_182'], color = '#e60202', linewidth = 3)
plt.plot(datos1.index, datos1['EMA_10'], color = '#000000', linewidth = 1)
plt.plot(datos1.index, datos1['EMA_55'], color = '#039709', linewidth = 2)
plt.fill_between(datos1.index, datos1['Close'], datos1['Low'].min(), where = datos1['is_bullish'], alpha = 0.5, color = '#09f613')
plt.fill_between(datos1.index, datos1['Close'], datos1['Low'].min(), where = datos1['is_bearish'], alpha = 0.32, color = '#df0808')
plt.scatter(x = df_test1.index, y = df_test1["Buy_Signal"], marker = '^')
plt.scatter(x = df_test1.index, y = df_test1["Sell_Signal"], marker = 'v')
plt.setp(ax1.get_xticklabels(), visible = False)
ax2 = plt.subplot(412, sharex = ax1)
plt.plot(datos1.index, datos1['histogram'])
plt.fill_between(datos1.index, datos1['histogram'], y2 = 0, where = (datos1['histogram'].shift(-1) > datos1['histogram']) & (datos1['histogram'] >= 0), color = '#10ed19', interpolate = True)
plt.fill_between(datos1.index, datos1['histogram'], y2 = 0, where = (datos1['histogram'].shift(-1) < datos1['histogram']) & (datos1['histogram'] <= 0), color = '#db1c1c', interpolate = True)
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(413, sharex = ax1)
plt.plot(datos1.index, datos1['Position_Sum'])
plt.plot(df_test1.index, df_test1['Cum_prod'])
plt.setp(ax3.get_xticklabels(), visible = False)
ax4 = plt.subplot(414, sharex = ax1)
plt.plot(back_test1.index, back_test1.Cash_USDT)
plt.grid(True)
plt.show()