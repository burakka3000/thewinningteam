import pandas as pd
import datetime
import CTG.Portfolio as pf
import CTG.data as dt
import CTG.Order as ord

class Interface:
    def __init__(self, initial_balance):
        self.Data = dt.Data()
        print('initialising portfolio...')
        self.Portfolio = pf.Portfolio(balance = initial_balance, data = self.Data)
        self.Log = Logbook()

        while True:
            run = input('Check stock price[S], check portfolio[P], place order[O] or get logbook[L]? [exit] to exit ')
            # get data
            if run == 'S':
                self.Data.get_data()
                print(self.Data.summary)

            # check portfolio
            elif run == 'P':
                print('Returning portfolio statistics')
                self.Portfolio.get_summary()
            # place order
            elif run == 'O':
                print('please specify order')
                order_type = input('what is the order type: [buy/sell] ')
                stock = input('input stock ticker: ')
                volume = float(input('enter volume: '))
                try:
                    limit = float(input('enter limit price: '))
                    new_order = ord.Order(type = order_type, stock = stock, volume = volume, portfolio = self.Portfolio, data =self.Data, limit = limit)
                except:
                    new_order = ord.Order(type = order_type, stock = stock, volume = volume, portfolio = self.Portfolio, data =self.Data)

                self.Portfolio.execute_order(new_order,self.Log)
                self.Portfolio.get_summary()

            # get history
            elif run == 'L':
                print(self.Log.get_log())

            elif run == 'exit':
                break

class Logbook:
    def __init__(self):
        self.df = pd.DataFrame(columns=['time','stock','volume','order_success','cash','stock_value','total_value'])

    def get_log(self):
        return self.df

    def update_log(self,stock_name, volume,order_success, portfolio):
        self.df = self.df.append({'time': datetime.datetime.now(),
                                  'stock':stock_name,
                                  'volume':volume,
                                  'order_success': order_success,
                                  'cash': portfolio.get_balance(),
                                  'stock_value': portfolio.get_stock_value(),
                                  'total_value': portfolio.get_balance() + portfolio.get_stock_value()
                                 },ignore_index=True)


