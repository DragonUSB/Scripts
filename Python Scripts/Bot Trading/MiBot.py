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
datos = datos[['Close_Timestamp', 'Open', 'High',  'Low', 'Close', 'Volume', 'Ignore']].copy()
datos.set_index('Close_Timestamp', inplace = True)

# Media Movil Exponencial
def EMA(df, n):
    df['EMA_' + str(n)] = df['Close'].ewm(span = n, min_periods = n - 1, adjust = False).mean()
    return df

# Moving Average Convergence Divergence
def MACD(df, f, s, sig, name):
    EMA1 = df['Close'].ewm(span = f, min_periods = f - 1, adjust = False).mean()
    EMA2 = df['Close'].ewm(span = s, min_periods = s - 1, adjust = False).mean()
    df['MACD_' + name] = EMA1 - EMA2
    EMA3 = df['MACD_' + name].ewm(span = sig, min_periods = sig - 1, adjust = False).mean()
    df['Histogram_' + name] = df['MACD_' + name] - EMA3
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

# Confluence Zones
confluence_level = 3
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

UpDown = 0
list = [0]
for i in range(1, len(datos)):
    d0, d1 = datos.Close[i], datos.Close[i-1]
    if d0 > d1:
        UpDown = max(1, UpDown + 1)
    elif d0 < d1:
        UpDown = min(-1, UpDown - 1)
    else:
        UpDown = 0
    list.append(UpDown)
list = pd.Series(list, index = datos.index, name = 'UpDown')
datos = datos.join(list)

# Rate of Change (ROC)
def ROC(df, n):
    M = df['Close'].diff(n - 1)
    N = df['Close'].shift(n - 1)
    ROC = pd.Series((M / N) * 100, name = 'ROC_' + str(n))
    df = df.join(ROC)
    return df

# RSI
def RSI(df, c, n):
    df['diff'] = df[c].diff(periods = 1)
    # df.dropna(inplace = True)
    df['sub'] = df['diff'][df['diff'] > 0]
    df['baj'] = abs(df['diff'][df['diff'] <= 0])
    df.fillna(value = 0, inplace = True)
    media_sub = df['sub'].rolling(window = n).mean()
    media_baj = df['baj'].rolling(window = n).mean()
    RSI = pd.Series(100 - (100 / (1 + (media_sub / media_baj))), name = 'RSI_' + str(n))
    df = df.join(RSI)
    df.drop(columns = ['diff','sub','baj'], inplace = True)
    return df

#  Percent Rank
def PercentRank(df, n):
    pctrank = lambda x: pd.Series(x).rank(pct = False).iloc[-1]
    percentrank = df['ROC_2'].rolling(window = n, center = False).apply(pctrank, raw = True)
    PercentRank = pd.Series(percentrank, name = 'PercentRank')
    df = df.join(PercentRank)
    return df

datos = RSI(datos, 'Close', 3)
datos = RSI(datos, 'UpDown', 2)
datos = ROC(datos, 2)
datos = PercentRank(datos, 100)

# Connors RSI
def CRSI(df):
    CRSI = pd.Series((df['RSI_3'] + df['RSI_2'] + df['PercentRank']) / 3, name = 'CRSI')
    df = df.join(CRSI)
    return df

datos = CRSI(datos)
Nivel_30 = pd.Series(datos['Ignore'] * 0 + 30, name = 'Nivel_30')
Nivel_70 = pd.Series(datos['Ignore'] * 0 + 70, name = 'Nivel_70')
datos = datos.join(Nivel_30)
datos = datos.join(Nivel_70)

# Crear Senales
datos['side'] = np.nan

histogram_bool = ((datos['histogram'].shift(-1) > datos['histogram']) & (datos['histogram'] >= 0)) | ((datos['histogram'].shift(-1) < datos['histogram']) & (datos['histogram'] <= 0))
long_signals = ((histogram_bool == True) & (datos['histogram'] >= 0) & (datos['CRSI'] > 70)) | (
                (histogram_bool == True) & (datos['histogram'] <= 0) & (datos['CRSI'] > 70))
short_signals =  (histogram_bool == False) & (datos['CRSI'] < 30)

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
        initial_cash = initial_cash + precio * f_unidades
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
fig.subplots_adjust(hspace = 0.1)
ax1 = plt.subplot(511)
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
ax2 = plt.subplot(512, sharex = ax1)
plt.plot(datos.index, datos['histogram'])
plt.fill_between(datos.index, datos['histogram'], y2 = 0, where = (datos['histogram'].shift(-1) > datos['histogram']) & (datos['histogram'] >= 0), color = '#10ed19', interpolate = True)
plt.fill_between(datos.index, datos['histogram'], y2 = 0, where = (datos['histogram'].shift(-1) < datos['histogram']) & (datos['histogram'] <= 0), color = '#db1c1c', interpolate = True)
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(513, sharex = ax1)
plt.plot(datos.index, datos['CRSI'])
plt.plot(datos.index, datos['Nivel_30'], color = 'r')
plt.plot(datos.index, datos['Nivel_70'], color = 'r')
plt.setp(ax3.get_xticklabels(), visible = False)
ax4 = plt.subplot(514, sharex = ax1)
plt.plot(datos.index, datos['Position_Sum'])
plt.plot(df_test.index, df_test['Cum_prod'])
plt.setp(ax4.get_xticklabels(), visible = False)
ax5 = plt.subplot(515, sharex = ax1)
plt.plot(back_test.index, back_test.Cash_USDT)
plt.grid(True)
plt.show()

# Grafico con matplotlib acotando los dias
datos1 = datos.iloc[-int(len(datos) / 2):,:]
df_test1 = df_test.iloc[-int(len(datos) / 2):,:]
back_test1 = back_test.iloc[-int(len(datos) / 2):,:]
fig = plt.figure(figsize = (12, 6))
fig.suptitle(f'Confluence Zones para {f_tick}{tick}')
fig.subplots_adjust(hspace = 0.1)
ax1 = plt.subplot(511)
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
ax2 = plt.subplot(512, sharex = ax1)
plt.plot(datos1.index, datos1['histogram'])
plt.fill_between(datos1.index, datos1['histogram'], y2 = 0, where = (datos1['histogram'].shift(-1) > datos1['histogram']) & (datos1['histogram'] >= 0), color = '#10ed19', interpolate = True)
plt.fill_between(datos1.index, datos1['histogram'], y2 = 0, where = (datos1['histogram'].shift(-1) < datos1['histogram']) & (datos1['histogram'] <= 0), color = '#db1c1c', interpolate = True)
plt.setp(ax2.get_xticklabels(), visible = False)
ax3 = plt.subplot(513, sharex = ax1)
plt.plot(datos1.index, datos1['CRSI'])
plt.plot(datos1.index, datos1['Nivel_30'], color = 'r')
plt.plot(datos1.index, datos1['Nivel_70'], color = 'r')
plt.setp(ax3.get_xticklabels(), visible = False)
ax4 = plt.subplot(514, sharex = ax1)
plt.plot(datos1.index, datos1['Position_Sum'])
plt.plot(df_test1.index, df_test1['Cum_prod'])
plt.setp(ax4.get_xticklabels(), visible = False)
ax5 = plt.subplot(515, sharex = ax1)
plt.plot(back_test1.index, back_test1.Cash_USDT)
plt.grid(True)
plt.show()