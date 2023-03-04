import config
from binance.client import Client
from binance.helpers import round_step_size

client = Client(config.API_KEY, config.API_SECRET, tld = 'com')

coin1 = 'UNI'
coin2 = 'USDT'
par = coin1 + coin2

symbol_info = client.get_symbol_info(par)
symbol_info = symbol_info['filters']

for m in symbol_info:
    for n in m:
        if n == 'tickSize':
            tickSize = float(m[n])
        elif n =='minNotional':
            minNotional = float(m[n])

print(f'tickSize = {tickSize} {coin1}')
print(f'minNotional = {minNotional} {coin2}')

amount = float(client.get_asset_balance(coin1, recvWindow = 10000)['free'])
rounded_amount = round_step_size(amount, tickSize)

print(f'amount = {amount} {coin1}')
print(f'rounded amount = {rounded_amount} {coin1}')