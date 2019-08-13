import numpy as np
import pandas as pd
import Logbook as lg

class Order:
    def __init__(self,type, stock, volume, data, portfolio, limit = 1000000, stop = 0):
        self.type = type
        self.stock = stock
        self.volume = volume
        if type == 'sell':
            self.volume = -self.volume
        self.data = data
        self.portfolio = portfolio
        self.limit = limit # If the current stock price is higher than the limit, the owner is not allowed to buy it
        self.stop = stop # If the current stock price is lower that the stop, the owner is not allowed to sell it

    def check_possible(self):
        if self.type == 'sell':
            try:
                if (-1*self.volume)> self.portfolio.get_stocks()[self.stock]:
                    print ('not enough stocks')
                    return False
            except:
                print('stock not in portfolio')
                return False

            if (self.data.get_summary()< self.stop):
                print('Order has been stopped')
                return False

        elif (self.data.get_summary()> self.limit):
            print('Order has been limited')
            return False

        elif (self.volume*self.data.get_summary())>self.portfolio.get_balance():
            print('Insufficient funds')
            return False

        return True

    def execute(self):
        if self.check_possible():
            self.status = 'succeeded'
            self.portfolio.update_balance(-1*self.volume*self.data.get_summary())
            self.portfolio.update_stocks(stock_name=self.stock, number_of_stocks=self.volume)
        else:
            self.status = 'failed'
        lg.get_log()
        lg.update_log(self, self.stock, self.volume, self.status, self.portfolio)
