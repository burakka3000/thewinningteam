import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, balance = 0):
        self.balance = balance # float containing balance on account in EUR
        self.stocks = pd.DataFrame(columns=['stock','count']) # dataframe containing the stocks and the number owned, first column is stock name, second is count
        self.owner = [] # depicts owner of portfolio

    def __repr__(self):
        return 'Portfolio of ' + self.owner.get_name

    def get_balance(self):
        return self.balance

    def get_owner(self):
        return self.owner

    def get_stocks(self):
        return self.stocks

    def update_balance(self, cash_change):
        # changes the cash balance
        if self.balance>cash_change:
            self.balance += cash_change
        else:
            Exception('Not enough funds, should be checked before')

    def update_stocks(self, stock_name, number_of_stocks):
        # checks if stock exists, if not add it, if it does change the number of stocks
        if stock_name in self.stocks.stock:
            self.stocks.loc[,'count']



