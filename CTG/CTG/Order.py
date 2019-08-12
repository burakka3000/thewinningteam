import pandas as pd
import numpy as np

class Order:
    def __init__(self, order_type, stock_name, stock_volume, Portfolio, data):
        self.order_type = order_type
        self.stock_name = stock_name
        self.stock_volume = stock_volume
        self.portfolio = Portfolio
        self.data = data

    def __repr__(self):
        return 'Order of ' + self.owner.get_name

    def balance_check(self):
        if self.order_type == "sell":
            self.stock_volume = - self.stock_volume
            self.cashflow = - self.stock_volumne * self.data.get_summary('price')
            if - self.stock_volume <= self.portfolio.stock_overview[self.stock_name]:
                Exception('Not enough stocks, check the number of stock to sell')
        if self.order_type == "buy":
            self.stock_volume = self.stock_volume
            self.cashflow = - self.stock_volumne * self.data.get_summary('price')
            if - self.cashflow >= self.portfolio.balance:
                Exception('Not enough stocks, check the number of stock to sell')

        self.portfolio.update_balance(self.cashflow)
        self.portfolio.update_stocks(self.stock_name, self.stock_volume)
