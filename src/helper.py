import yfinance as yf
import os
import src.fennel as f
import src.robinhood as r
import src.public as p
import src.firstradeutil as ft
import src.color as clrs
import src.helper as utils

def YFgetStockPrice(ticker):
    try:
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        return float(last_quote)
    except:
        #print(ticker_yahoo)
        return -1