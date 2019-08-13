class Order:
    def __init__(self,type, stock, volume, data, portfolio, limit = False):
        self._type = type
        self.stock = stock
        self.volume = volume
        if type == 'sell':
            self.volume = -self.volume
        self.data = data
        self.portfolio = portfolio
        self.limit = limit

    @property
    def type(self):
        return self._type
    @property
    def stock(self):
        return self.stock
    @property
    def  volume(self):
        return self.volume
    @property
    def limit(self):
        return self.limit
    @property
    def portfolio(self):
        return self.portfolio
    @property
    def portfolio(self):
        return self.data


    def check_possible(self):
        if self.type == 'sell':
            try:
                if (-1*self.volume)> self.portfolio.get_stocks()[self.stock]:
                    print ('not enough stocks')
                    return False
            except:
                print('stock not in portfolio')
                return False

            if (self.data.summary.loc(1, self.stock)< self.limit):
                print('Sell order has been limited as the stock price is too low.')
                return False

        elif self.limit != False:
            if (self.data.summary.loc(1, self.stock)()> self.limit):
                print('Buy order has been limited as the stock price is too high')
                return False

        elif (self.volume*self.data.summary.loc(1, self.stock))>self.portfolio.get_balance():
            print('Insufficient funds')
            return False

        return True
