import pandas as pd
import numpy as np

class Order:
    def __init__(self, order_type, stock_name, stock_volumn):
        self.order_type = order_type
        self.stock_name = stock_name
        self.stock_volumn = stock_volumn
        self.status = status # processing/success/failed

        # self.balance = balance # float containing balance on account in EUR
        # self.stocks = pd.DataFrame(columns=['stock','count']) # dataframe containing the stocks and the number owned, first column is stock name, second is count
        # self.owner = [] # depicts owner of portfolio

    def __repr__(self):
        return 'Portfolio of ' + self.owner.get_name

    def get_actions(self):
        # userinput
        stock_name = input("")
        number_of_stocks = input("")
        buy_or_sell = input("")
        if buy_or_sell = "sell":
            cash_mark = -1
        if buy_or_sell = "buy":
                cash_mark = 1
        else:
            Exception('Not enough funds, should be checked before')
        stock_price = data.get_data = pd.DataFrame # get the price of the stock
        cashchange = stock_price * number_of_stocks * cash_mark
        return self.actions

    def get_status(self):
        return self.status
