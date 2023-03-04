import config
from binance.client import Client
from binance.enums import *
from binance.helpers import round_step_size

client = Client(config.API_KEY, config.API_SECRET, tld = 'com')

symbol = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'UNIUSDT', 'LINKUSDT', 'LUNAUSDT', 'BATUSDT', 'DASHUSDT', 'DOGEUSDT', 'CAKEUSDT']

for symbol_str in symbol:
    symbol_info = client.get_symbol_info(symbol_str)
    print(symbol_info['symbol'])
    asset = symbol_info['symbol']
    asset = asset.split('USDT')
    symbol_info_filters = symbol_info['filters']

    balance = client.get_asset_balance(asset[0], recvWindow = 40000)['free']
    print('balance = ' + balance)

    for m in symbol_info_filters:
        for n in m:
            if n == 'tickSize':
                tickSize = float(m[n])
                print('tickSize = ' + str(tickSize))
            elif n =='minNotional':
                minNotional = float(m[n])
                print('minNotional = ' + str(minNotional))
    
    MaxSell = round_step_size(float(balance) * 1.001, tickSize)
    print('Max Sell = ' + str(MaxSell))