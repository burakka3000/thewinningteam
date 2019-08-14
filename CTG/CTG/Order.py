class Order:
    def __init__(self,type: str, stock, volume, data, limit = False) -> None:
        self._type = type
        self._stock = stock
        self._volume = volume
        if type == 'sell':
            self._volume = -volume
        else:
            self._volume = volume
        self._data = data
        self._limit = limit



    def check_possible(self) -> bool:
        if self._type == "sell" or "buy":
            pass
        else:
            print("Check your order type")
            return False
        if self._stock not in stocks:
            print("The stock does not exist")
            return False
        if self._volume < 1:
            print("Check your order volume")
            return False
        if self._type =="sell":
            if self._data.summary.loc[self._data.summary['Ticker']==self._stock,'Price'].values < self._limit:
                print('Sell order has been limited as the stock price is too low.')
                return False
        elif self._data.summary.loc[self._data.summary['Ticker']==self._stock,'Price'].values:
            print('Buy order has been limited as the stock price is too high')
            return False


    def cal_stock_price(self):
        stock_price = self._data.summary.loc[self._data.summary['Ticker']==self._stock,'Price'].values
        return stock_price

    def calc_cash_flow(self):
        cash_flow = - self.stock_price * self._volume
        return cash_flow


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
        return self.cal_stock_price()
    @property
    def cash_flow(self):
        return self.calc_cash_flow()
