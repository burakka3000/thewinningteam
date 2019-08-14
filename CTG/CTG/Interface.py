import pandas as pd
import datetime
import CTG.Portfolio as pf
import CTG.data as dt
import CTG.Order as ord

class Interface:
    "Interface class is used to communicate with all classes and receive user input"
    def __init__(self, initial_balance):
        self.Data = dt.Data()
        print('initialising portfolio...')
        self.Data.get_data()
        self.Portfolio = pf.Portfolio(balance = initial_balance, data = self.Data)
        self.Log = Logbook()

        while True:
            self.Data.update()
            run = input('Check stock price[S], check portfolio[P], place order[O] or get logbook[L]? [exit] to exit ')
            # get data
            if run == 'S':
                print(self.Data.summary)

            # check portfolio
            elif run == 'P':
                print('Returning portfolio statistics')
                self.Portfolio.get_summary()
            # place order
            elif run == 'O':
                print('please specify order')
                while True:
                    order_type = input('what is the order type: [buy/sell] ')
                    if order_type.lower() in ["buy", "sell"]:
                        break
                    print("Check your order type")
                while True:
                    stock = input('input stock ticker: ')
                    if stock in ['AAPL','MSFT', 'WFC', 'JNJ', 'DIS']:
                        break
                    print("Check your stock symbol")
                while True:
                    volume = float(input('enter volume: '))
                    if volume >0:
                        break
                    print("Volume can't be lower than 1.")

                    new_order = ord.Order(type = order_type, stock = stock, volume = volume, data =self.Data)

                self.Portfolio.execute_order(new_order,self.Log)
                self.Portfolio.get_summary()

            # get history
            elif run == 'L':
                print(self.Log.get_log())
                print('Remember: jetfuel cant melt steel beams')

            # exit loop
            elif run == 'exit':
                print('Before you go: 9/11 was an inside job')
                break

class Logbook:
    def __init__(self):
        self.df = pd.DataFrame(columns=['time','stock','volume','order_success','cash','stock_value','total_value'])

    def get_log(self):
        return self.df

    def update_log(self,stock_name, volume,order_success, portfolio):
        "Updates log after an order has been placed"
        self.df = self.df.append({'time': datetime.datetime.now(),
                                  'stock':stock_name,
                                  'volume':volume,
                                  'order_success': order_success,
                                  'cash': portfolio.balance,
                                  'stock_value': portfolio.get_stock_value(),
                                  'total_value': portfolio.balance + portfolio.get_stock_value()
                                 },ignore_index=True)


