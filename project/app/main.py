from fastapi import FastAPI

from app.lib.binance import (
    get_market_depth,
    get_all_tickers,
    get_historical_trades,
    get_recent_trades,
    get_status,
    get_exchange_info,
    get_orderbook_tickers,
    get_ticker,
    get_products,
)
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get("/status")
def status():
    # return {"some": test()}
    return JSONResponse(get_status())


@app.get("/getticker")
def getticker():
    return JSONResponse(get_ticker())


@app.get("/getproducts")
def getproducts():
    return JSONResponse(get_products())


@app.get("/getalltickers")
def getalltickers():
    """problem??"""
    return JSONResponse(get_all_tickers())


@app.get("/getorderbooktickers")
def getorderbooktickers():
    return JSONResponse(get_orderbook_tickers())


@app.get("/getmarketdepth")
def getmarketdepth():
    """problem??"""
    return JSONResponse(get_market_depth())


@app.get("/getrecenttrades")
def getrecenttrades():
    """problem??"""
    return JSONResponse(get_recent_trades())


@app.get("/gethistoricaltrades")
def gethistoricaltrades():
    """problem??"""
    return JSONResponse(get_historical_trades())


@app.get("/getexchangeinfo")
def getexchangeinfo():
    """problem??"""
    return JSONResponse(get_exchange_info())


@app.get("/test")
def test():
    return PlainTextResponse("ALL IS OK")
