import requests
import pandas as pd
from colorama import init, Back

# use Colorama to make Termcolor work on Windows too
init(autoreset=True)

re = requests.get('https://api.binance.com/api/v3/exchangeInfo')
data = re.json()
symbols = data['symbols']

symbol_list = []
status_list = []

for item in symbols:
    symbol_list.append(item['symbol'])
    status_list.append(item['status'])

def filter_stock(symbol_list):
    stock = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'UNIUSDT', 'LINKUSDT', 'LUNAUSDT', 'BATUSDT', 'DASHUSDT', 'DOGEUSDT', 'CAKEUSDT']
    return True if symbol_list in stock else False

# uni_symbol = filter(lambda x : 'UNIUSDT' in x, symbol_list)
uni_symbol = filter(filter_stock, symbol_list)
stock_symbol_list = list(uni_symbol)

interval = ["1d", "4h"]

for interval_str in interval:

    for symbol_str in stock_symbol_list:
    
        print(Back.GREEN + '..................................................')
        print(Back.GREEN + f'Downloading {symbol_str} data for {interval_str}')
        url = 'https://api.binance.com/api/v3/klines'
        headers = {'accept': 'application/json'}
        doc_columns = ['Open_Time', 'Open', 'High', 'Low', 'Close', 'Volume',
                       'Close_Time', 'Quote_asset_vol', 'Number_trades', 'Toker_buy_base',
                       'Toker_buy_quote', 'Ignore']
    
        main_df = pd.DataFrame(columns = doc_columns)
    
        pagination = True
        initial_round = True
        last_end_time = None
    
        while pagination:
        
            try:
                if initial_round:
                    print('Ronda Inicial')
                    body = {"symbol": symbol_str, "interval": interval_str, "limit": "1000"}
                    initial_round = False
                else:
                    body = {"symbol": symbol_str, "interval": interval_str, "limit": "1000", "endTime": end_time}
                
                response = requests.get(url, headers = headers, params = body)    
                data = response.json() 
                print('Data requested')    
                
                df = pd.DataFrame(data, columns = doc_columns)
                df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit = 'ms')
                df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit = 'ms')
                
                main_df = pd.concat([main_df, df])
                main_df = main_df.sort_values(by = 'Open_Timestamp', ascending = True) 
                end_time = str(main_df['Open_Time'].iloc[0])
            
                if last_end_time == end_time:
                    print('Finishing fetching')
                    break
                
                last_end_time = end_time
            
            except:
                pagination = False
                
            filename = symbol_str + '_' + interval_str + '.csv'
            print(f'Saving {symbol_str} csv file')
            main_df.to_csv(filename)