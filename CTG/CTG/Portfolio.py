import pandas as pd
import numpy as np

class Portfolio:
    # Portfolio class
    # contains the balance and the stock overview of the current portfolio
    def __init__(self, balance = 0):
        self.balance = balance # float containing balance on account in EUR
        self.stock_overview = {} # Dictionairy containing the stocks and the number owned, first column is stock name, second is count
        self.owner = [] # depicts owner of portfolio

    def __repr__(self):
        return 'Portfolio object with '+ str(self.balance)

    def get_balance(self):
        return self.balance

    def get_owner(self):
        return self.owner

    def get_stocks(self):
        return self.stock_overview

    def update_balance(self, cash_change):
        # changes the cash balance
        if self.balance>cash_change:
            self.balance += cash_change
        else:
            Exception('Not enough funds, should be checked in order class')

    def update_stocks(self, stock_name, number_of_stocks):
        # checks if stock exists, if not add it, if it does change the number of stocks
        if stock_name in self.stock_overview:
            self.stock_overview[stock_name] += number_of_stocks
        else:
            self.stock_overview[stock_name] = number_of_stocks

    def get_summary(self):
        # returns string with summary of portfolio
        print( 'current balance is: '+ str(self.balance))
        print('stock; volume')
        print(self.stock_overview)





