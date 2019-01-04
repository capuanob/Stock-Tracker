from file_loader import *
import datetime
import pandas as pd
import pandas_datareader.data as web


class Stock:
    full_name = ""
    symbol = ""

    def __init__(self, full_name, symbol):
        self.full_name = full_name
        self.symbol = symbol


class Stock_List:
    symbol_loader = File_Loader()
    stock_list = list()
    data = ""

    def is_empty(self):
        return len(self.stock_list) == 0

    def find_similar(self):
        """yuh"""
        # TODO: Implement this one

    def add_stock(self, symbol):
        index = -1
        full_name = ""

        for i, val in enumerate(self.symbol_loader.symbols):
            if val == symbol:
                index = i
                break

        if index == -1:
            self.find_similar()
        else:
            full_name = self.symbol_loader.full_names[index]
            new_stock = Stock(full_name, symbol)
            if new_stock in self.stock_list:
                print("You're already following this stock.")
                return
            self.stock_list.append(new_stock)

    def check_stocks(self):
        for stock in self.stock_list:
            print(stock.full_name)
            self.get_stock_data(stock.symbol)
            print("\n\n")

    def reset(self):
        self.stock_list = list()

    def delete_stock(self, symbol):
        for i, val in enumerate(self.stock_list):
            if val.symbol == symbol:
                del(self.stock_list[i])
                break
        else:
            print("You cannot unfollow a stock that you do not already follow.")

    def get_stock_data(self, symbol):
        now = datetime.datetime.now()
        start = datetime.datetime(now.year, now.month, now.day)
        print(start)
        df = web.DataReader(symbol, 'yahoo', start, start)
        print(df.head())
