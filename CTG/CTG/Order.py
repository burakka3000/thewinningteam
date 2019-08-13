
class Order:
<<<<<<< HEAD
    def __init__(self, order_type, stock_name, stock_volume, Portfolio, data):
        self.order_type = order_type
        self.stock_name = stock_name
        self.stock_volume = stock_volume
        self.portfolio = Portfolio
=======
    def __init__(self,type, stock, volume, data, portfolio):
        self.type = type
        self.stock = stock
        self.volume = volume
        if type == 'sell':
            self.volume = -self.volume
>>>>>>> b4bb3ae6fdd02ac917bb04a576c1a430a10ae418
        self.data = data
        self.portfolio = portfolio

<<<<<<< HEAD
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
=======
    def check_possible(self):
        if self.type == 'sell':
            try:
                if (-1*self.volume)> self.portfolio.get_stocks()[self.stock]:
                    print ('not enough stocks')
                    return False
            except:
                print('stock not in portfolio')
                return False
        elif (self.volume*self.data.get_summary())>self.portfolio.get_balance():
            print('Insufficient funds')
            return False
        return True

    def execute(self):
        if self.check_possible():
            self.portfolio.update_balance(-1*self.volume*self.data.get_summary())
            self.portfolio.update_stocks(stock_name=self.stock, number_of_stocks=self.volume)


>>>>>>> b4bb3ae6fdd02ac917bb04a576c1a430a10ae418
