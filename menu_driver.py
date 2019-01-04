from stocks import Stock_List


class Menu_Driver:
    my_stocks = Stock_List()

    def __init__(self):
        try:
            self.load_stocks()
        except Exception:
            pass

    def run_menu_driver(self):
        running = True
        print("Welcome to Stock Tracker. To begin, choose one of the following.")
        while running:
            running = self.print_menu()

    def print_menu(self):
        print("\t1. Check my stocks.")
        print("\t2. Follow a new stock.")
        print("\t3. Unfollow a stock.")
        print("\t4. Reset my stocks.")
        print("\t5. Quit program.")
        return self.take_menu_input()

    def take_numerical_input(self):
        try:
            response = int(input())
            return response
        except ValueError:
            print("Please enter your choice as a number (e.g. '1').")
            self.take_numerical_input()

    def take_menu_input(self):
        input = self.take_numerical_input()

        if input == 1:
            self.check_stocks()
        elif input == 2:
            self.add_stock()
        elif input == 3:
            self.delete_stock()
        elif input == 4:
            self.reset_stocks()
        elif input == 5:
            self.save_stocks()
            return False
        else:
            self.print_menu()
        return True

    def save_stocks(self):
        if not self.my_stocks.is_empty():
            file = open("myStocks.txt", "w")
            for stock in self.my_stocks.stock_list:
                file.write(f"{stock.symbol}\n")
            file.close()

    def load_stocks(self):
        with open("myStocks.txt") as f:
            for line in f:
                self.my_stocks.add_stock(line[:-1])

    def check_stocks(self):
        if self.my_stocks.is_empty():
            print("You are not currently following any stocks.")
        else:
            self.my_stocks.check_stocks()

    def add_stock(self):
        print("What is the NASDAQ symbol for the stock you would like to follow?")
        symbol = input("Symbol: ")
        self.my_stocks.add_stock(symbol)

    def delete_stock(self):
        print("What is the NASDAQ symbol for the stock you would like to unfollow?")
        symbol = input("Symbol: ")
        self.my_stocks.delete_stock(symbol)

    def reset_stocks(self):
        self.my_stocks.reset()
        print("You have unfollowed all saved stocks.")
