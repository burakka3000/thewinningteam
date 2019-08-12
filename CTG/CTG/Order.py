class Order:
    def __init__(self,type, stock, volume, data, portfolio):
        self.type = type
        self.stock = stock
        self.volume = volume
        self.data = data
        self.portfolio = portfolio

    def check_possible(self):
        if self.type == 'sell':
            try:
                if self.volume> self.portfolio.get_stocks()[self.stock]:
                    print ('not enough stocks')
                    return False
            except:
                print('not enough stocks')
                return False

        if (self.volume*self.data.get_summary())>self.portfolio.get_balance():
            print('Insufficient funds')
            return False
        return True

    def execute(self):
        if self.check_possible():
            self.portfolio.update_balance(self.volume*self.data.get_summary())
            self.portfolio.update_stocks(stock_name=self.stock, number_of_stocks=self.volume)


