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
