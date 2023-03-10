from tradingview_ta import TA_Handler, Interval
import time
from datetime import datetime
import config
from binance.client import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET, tld='com')


now = datetime.now()
fecha = now.strftime("%d-%m-%y %H:%M:%S")
lista = client.get_all_tickers()
#lista = ["UNIUSDT","UNIBTC"]
strongBuy_list = []
strongSell_list = []
for i in lista:
    if (i['symbol'][-4:] != 'USDT'):
        continue
    tesla = TA_Handler()
    tesla.set_symbol_as(i['symbol'])
    #tesla.set_symbol_as(i)
    tesla.set_exchange_as_crypto_or_stock("BINANCE")
    tesla.set_screener_as_crypto()
    tesla.set_interval_as(Interval.INTERVAL_1_HOUR)
    print(i['symbol'])
    #print(i)
    try:
      print(tesla.get_analysis().summary)
    except Exception as e:
      print("No Data")
      continue
    if((tesla.get_analysis().summary)["RECOMMENDATION"])=="STRONG_BUY":
        print(f" Compar más fuerte {i}", fecha)
        strongBuy_list.append(i['symbol'])
    elif((tesla.get_analysis().summary)["RECOMMENDATION"])=="STRONG_SELL":
        print(f" Compar más fuerte {i}", fecha)
        strongSell_list.append(i['symbol'])
        
print("*** STRONG BUY LIST ***")

print(strongBuy_list)

print("*** STRONG SELL LIST ***")

print(strongSell_list)