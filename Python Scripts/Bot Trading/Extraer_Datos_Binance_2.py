import pandas as pd
import requests
import csv
import matplotlib.pyplot as plt
from tqdm.auto import tqdm, trange

#%matplotlib inline

symbol = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'UNIUSDT', 'LINKUSDT', 'LUNAUSDT', 'BATUSDT', 'DASHUSDT', 'DOGEUSDT', 'CAKEUSDT', 'MATICUSDT']
tick_interval = ['1d', '4h', '1h']

def get_candles(start = '', symbol = 'BTCUSDT', tick_interval = '1d', limit = 1000):
    base_url = 'https://api.binance.com/'
    endpoint = 'api/v3/klines?'
    if start:
        query = 'symbol=' + symbol + '&interval=' + tick_interval + '&startTime=' + str(start) + '&limit=' + str(limit)
    else:
        query = 'symbol=' + symbol + '&interval=' + tick_interval + '&limit=' + str(limit)
    candles = requests.get(base_url + endpoint + query).json()
    return candles, candles[-1][6]  # return candles and last close time in a tuple

def get_all_candles_from_start(symbol, tick_interval):  # devuelve una lista de velas, cada vela es una lista tb
    start=1502942400000  # 17 de agosto de 2017
    _, last_time = get_candles(start = '', symbol = symbol , tick_interval = tick_interval, limit = 1000)
    candles = []
    while start < last_time:
        i_candles, next_hop = get_candles(start, symbol, tick_interval)
        candles = candles + i_candles
        start = next_hop
    return candles

for interval_str in tick_interval:

    for i in tqdm(range(len(symbol)), desc = 'Descargando', colour = 'red'):

        symbol_str = symbol[i]
        candles = get_all_candles_from_start(symbol_str, interval_str)
        columns = ['Open_Time', 'Open',  'High', 'Low', 'Close', 'Volume', 'Close_Time', 'Quote', 'Trades', 'Takers_Buy_Base', 'Takers_Buy_Quote', 'Ignore']
        df = pd.DataFrame(candles, columns = columns)
        df = df.sort_values('Close_Time')
        df.drop_duplicates(keep = 'last')
        df = df.astype(float)
        df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit = 'ms')
        df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit = 'ms')

        # Se guardan los datos en un archivo csv
        df.to_csv(f'{symbol_str}_{interval_str}.csv', index = False, header = True, quoting = csv.QUOTE_ALL)

        tqdm.write(f'Descargado y Grabado los datos de {symbol_str}_{interval_str}')

        # df['Close_Time'] = pd.to_datetime(df['Close_Time'], unit = 'ms')
        # #df['close_time'] = df['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
        # df = df.set_index('Close_Time')
        # df['Close'].plot(figsize = (12,6), label = symbol_str)
        # plt.title(f'Precio de {symbol_str}')
        # plt.legend()
        # plt.grid()
        # plt.show()