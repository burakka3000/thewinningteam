import CTG.Portfolio as pf
import CTG.data as dt
import CTG.Order as ord

class Interface:
    def __init__(self, initial_balance):
        self.Portfolio = pf.Portfolio(balance = initial_balance)
        self.Data = dt.Data()
        print('initialising portfolio...')

        while True:
            run = input('Check stock price[S], check portfolio[P] or place order[O]? [exit] to exit')
            # get data
            if run == 'S':
                choice1 = input('[price/plot]?')
                self.Data.get_data()
                if choice1 == 'price':
                    print('current price equals '+str(self.Data.get_summary(type= choice1)))
                elif choice1 == 'plot':
                    self.Data.get_summary(type=choice1)

            # check portfolio
            elif run == 'P':
                print('Returning portfolio statistics')
                self.Portfolio.get_summary()
            # place order
            elif run == 'O':
                print('please specify order')
                order_type = input('what is the order type: [buy/sell]')
                stock = input('input stock ticker: ')
                volume = float(input('enter volume: '))

                self.Data.get_data()
                new_order = ord.Order(type = order_type, stock = stock, volume = volume, portfolio = self.Portfolio, data =self.Data)
                new_order.execute()
                self.Portfolio.get_summary()

            elif run == 'exit':
                break


