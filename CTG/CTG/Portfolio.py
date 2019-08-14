class Portfolio:
    # Portfolio class
    # contains the balance and the stock overview of the current portfolio
    def __init__(self,data, balance = 0):
        self._balance = balance # float containing balance on account in EUR
        self._stock_overview = {} # Dictionairy containing the stocks and the number owned, first column is stock name, second is count
        self._owner = [] # depicts owner of portfolio
        self.data = data # data object

    def __repr__(self):
        return 'Portfolio object with '+ str(self._balance)

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @property
    def stock_overview(self):
        return self._stock_overview

    def get_stock_value(self):
        value = 0
        for stock in self._stock_overview:
            value += self._stock_overview[stock]* self.data.summary().loc[self.data.summary()['Ticker']==stock,'Price'].values
        return value

    # make this a setter function
    def update_balance(self, cash_change):
        # changes the cash balance
        if self._balance>cash_change:
            self._balance += cash_change
        else:
            raise Exception('Not enough funds, should be checked in order class')

    # make this a setter function
    def update_stocks(self, stock_name, number_of_stocks):
        # checks if stock exists, if not add it, if it does change the number of stocks
        if stock_name in self._stock_overview:
            self._stock_overview[stock_name] += number_of_stocks
        else:
            self._stock_overview[stock_name] = number_of_stocks

    # change this to __str__ function
    def __str__(self):
        # returns string with summary of portfolio
        print( 'current balance is: '+ str(self.balance))
        print('stock; volume')
        print(self.stock_overview)
        if self.stock_overview:
            print('stock value: ' + str(self.get_stock_value()))

    def execute_order(self, Order,Log):
        # executes order given order object
        if Order.check_possible():
            self.update_balance(-1 * Order.volume * self.data.summary.loc[self.data.summary['Ticker']==Order.stock,'Price'].values)
            self.update_stocks(Order.stock,Order.volume)
            Log.update_log(stock_name=Order.stock, volume=Order.volume, order_success='yes', portfolio = self)
        else:
            print('order failed')
            Log.update_log(stock_name=Order.stock, volume=Order.volume, order_success='no', portfolio = self)

    def check_order(self,Order):
        pass