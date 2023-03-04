import config
from binance.client import Client
from binance.enums import *
from binance.helpers import round_step_size
import time
import numpy as np

client = Client(config.API_KEY, config.API_SECRET, tld = 'com')

def buyAmount(coin, pair):
    balanceBuy = float(client.get_asset_balance(coin, recvWindow = 10000)['free'])
    close = float(client.get_symbol_ticker(symbol = pair)['price'])
    maxBuy = round(balanceBuy / close * .995, 8)
    return maxBuy

maxBuy = buyAmount('USDT', 'UNIUSDT')
print("\nEsto es lo maximo de UNI que puedes comprar: " + str(maxBuy) + '\n')

def sellAmount(coin):
    balanceSell = float(client.get_asset_balance(coin, recvWindow = 10000)['free'])
    maxSell = round(balanceSell * .995, 8)
    return maxSell

maxSell = sellAmount('UNI')
print("Esto es lo maximo de UNI que puedes vender: " + str(maxSell) + '\n')

symbolTicker = 'UNIUSDT'
quantity = 0.5
prev_symbolPrice = 0

list_of_tickers = client.get_all_tickers()
for tick_2 in list_of_tickers:
    if tick_2["symbol"] == symbolTicker:
        prev_symbolPrice = float(tick_2["price"])

symbol_info = client.get_symbol_info(symbolTicker)
symbol_info = symbol_info['filters']

for m in symbol_info:
    for n in m:
        if n == 'tickSize':
            tickSize = float(m[n])
        elif n =='minNotional':
            minNotional = float(m[n])

buyOrder = client.create_order(
    symbol = symbolTicker,
    side = 'BUY',
    type = 'STOP_LOSS_LIMIT',
    quantity = quantity,
    price = round_step_size(prev_symbolPrice*1.001,tickSize),
    stopPrice = round_step_size(prev_symbolPrice*1.002,tickSize),
    timeInForce = 'GTC'
)

while 1:
    time.sleep(5)

    list_of_tickers = client.get_all_tickers()
    for tick_2 in list_of_tickers:
        if tick_2["symbol"] == symbolTicker:
            current_symbolPrice = float(tick_2["price"])

    print("    Prev Price = " + str(prev_symbolPrice))
    print(" Current Price = " + str(current_symbolPrice))

    if ( prev_symbolPrice > current_symbolPrice):

        result = client.cancel_order(
            symbol = symbolTicker,
            orderId = buyOrder.get('orderId')
        )

        buyOrder = client.create_order(
            symbol = symbolTicker,
            side = 'BUY',
            type = 'STOP_LOSS_LIMIT',
            quantity = quantity,
            price = round_step_size(current_symbolPrice*1.001,tickSize),
            stopPrice = round_step_size(current_symbolPrice*1.002,tickSize),
            timeInForce = 'GTC'
        )

        prev_symbolPrice = current_symbolPrice