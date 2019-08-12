import pandas as pd
import numpy as np

class Order:
    def __init__(self, order_type, stock_name, stock_volume, Portfolio, data):
        self.order_type = order_type
        self.stock_name = stock_name
        self.stock_volume = stock_volume
        self.portfolio = Portfolio
        self.data = data

        self.status = "" # processing/success/failed

    def __repr__(self):
        return 'Order of ' + self.owner.get_name

    def balance_check(self):
        self.cashflow = 
        if self.order_type == "sell":
            if self.stock_volume <= self.portfolio.stock_overview[self.stock_name]:
                Exception('Not enough stocks, check the number of stock to sell')
        if self.order_type == "buy":
            if self.stock_volumne * self.data.get_summary('price') >= self.portfolio.balance:
                Exception('Not enough stocks, check the number of stock to sell')

    self.portfolio.update_balance()
    self.portfolio.update_stocks()


    def get_order_(self):
        return

        stock_price = data.get_data = pd.DataFrame # get the price of the stock
        cashchange = stock_price * number_of_stocks * cash_mark
        return self.actions

    def get_status(self):
        return self.status
