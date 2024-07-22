import yfinance as yf
import os

def YFgetStockPrice(ticker):
    try:
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()
        last_quote = data['Close'].iloc[-1]
        return float(last_quote)
    except:
        #print(ticker_yahoo)
        return -1