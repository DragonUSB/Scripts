import asyncio
import json

from binance import AsyncClient

async def main():
    
    client = await AsyncClient.create()
    symbol_info = await client.get_symbol_info('UNIUSDT')
    
    print(json.dumps(symbol_info, indent=2))

    await client.close_connection()
    
if __name__ == "__main__":
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())