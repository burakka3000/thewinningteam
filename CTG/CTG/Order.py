class Order:
    def __init__(self,type, stock, volume, data, limit = False):
        self._type = type
        self._stock = stock
        self._volume = volume
        if type == 'sell':
            self._volume = -volume
        else:
            self._volume = volume
        self._data = data
        self._limit = limit

    @property
    def type(self):
        return self._type
    @property
    def stock(self):
        return self._stock
    @property
    def  volume(self):
        return self._volume
    @property
    def limit(self):
        return self._limit
    @property
    def data(self):
        return self._data
    @property
    def stock_price(self):
        return self._stock_price
    @property
    def cash_flow(self):
        return self._cash_flow


    def check_possible(self):
        if self._type == 'sell':
            try:
                if (-1*self._volume)> self._portfolio.get_stocks()[self._stock]:
                    print ('not enough stocks')
                    return False
            except:
                print('stock not in portfolio')
                return False

            if self._data.summary.loc(1, self._stock)< self._limit:
                print('Sell order has been limited as the stock price is too low.')
                return False

        elif self._limit:
            if self._data.summary.loc(1, self._stock)()> self._limit:
                print('Buy order has been limited as the stock price is too high')
                return False

        elif (self._volume * self._data.summary().loc[self._data.summary()['Ticker']==self._stock,'Price'].values) > self.portfolio.get_balance():
            print('Insufficient funds')
            return False

        return True

    def stock_price(self):
        price = self._data.summary().loc[self._data.summary()['Ticker']==self._stock,'Price'].values)

    def cash_flow(self):
        return self._volume*

