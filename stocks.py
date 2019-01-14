from file_loader import *
from datetime import datetime, timedelta
from difflib import SequenceMatcher
import pandas as pd
import pandas_datareader.data as web


class Stock:
    full_name = ""
    symbol = ""

    def __eq__(self, other):
        return self.symbol == other.symbol

    def __init__(self, full_name, symbol):
        self.full_name = full_name
        self.symbol = symbol


class Stock_List:
    symbol_loader = File_Loader()
    stock_list = list()
    data = ""

    def is_empty(self):
        return len(self.stock_list) == 0

    def find_similar(self, symbol):
        mostSimilar = [0] * 2

        for val in self.symbol_loader.symbols:
            if SequenceMatcher(None, symbol, val).ratio() > mostSimilar[1]:
                mostSimilar[0] = val
                mostSimilar[1] = SequenceMatcher(None, symbol, val).ratio()
        print(f"Stock not found. Did you mean: {mostSimilar[0] }")

    def add_stock(self, symbol):
        index = -1
        full_name = ""

        for i, val in enumerate(self.symbol_loader.symbols):
            if val == symbol:
                index = i
                break

        if index == -1:
            self.find_similar(symbol)
        else:
            full_name = self.symbol_loader.full_names[index]
            new_stock = Stock(full_name, symbol)
            for stock in self.stock_list:
                if new_stock == stock:
                    print("You cannot follow a stock more than once.")
                    del new_stock
                    return
            self.stock_list.append(new_stock)

    def check_stocks(self):
        for stock in self.stock_list:
            print(stock.full_name)
            self.get_stock_data(stock.symbol)
            print("\n\n")

    def reset(self):
        self.stock_list = list()
        open("myStocks.txt", "w").close()

    def delete_stock(self, symbol):
        for i, val in enumerate(self.stock_list):
            if val.symbol == symbol:
                del(self.stock_list[i])
                break
        else:
            print("You cannot unfollow a stock that you do not already follow.")

    def get_stock_data(self, symbol):
        d = datetime.today()

        if d.weekday() >= 5:
            d = datetime.today() - timedelta(days=2)
            d = datetime(d.year, d.month, d.day, 17, 0, 0, 0)

        try:
            df = web.DataReader(symbol, 'yahoo', d, d)
            print(df)
        except Exception:
            print("Error connecting with Finance API.")
