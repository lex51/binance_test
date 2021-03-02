import os


from binance.client import Client

token = os.environ["TOKEN_BINANCE"]
sk = os.environ["SK_BINANCE"]
# HOST_BINANCE
sk = os.environ["HOST_BINANCE"]

client = Client(token, sk)


def get_status():
    return client.get_system_status()


def get_ticker():
    return client.get_ticker()


def get_all_tickers():
    return client.get_all_tickers()


def get_products():
    return client.get_products()


def get_orderbook_tickers():
    return client.get_orderbook_tickers()


def get_market_depth():
    return client.get_order_book(symbol="BNBBTC", limit=2)


def get_recent_trades():
    return client.get_recent_trades(symbol="BNBBTC", limit=1)


def get_historical_trades():
    return client.get_historical_trades(symbol="ETHBTC")


def get_exchange_info():
    return client.get_exchange_info()
