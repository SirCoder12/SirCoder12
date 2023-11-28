import yfinance as yf
import cwd
import pandas as pd 
cwd.cwd(".csv")

stock_data = pd.read_csv("nasdaq_screener_1694349309221.csv")
symbols = stock_data["Symbol"]
names = stock_data["Name"]

def info_in_all_stocks(key):
    for symbol, name in zip(symbols, names):
        stock = yf.Ticker(symbol)
        print({name: stock.info[key]})

def show_stock(stock_name):
    stock = yf.Ticker(stock_name)
    print(stock.info.keys())


info_in_all_stocks("dayHigh")