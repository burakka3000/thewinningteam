import CTG.CTG.Portfolio as pf
import CTG.CTG.data as dt

class Interface:
    def __init__(self, initial_balance):
        self.Portfolio = pf.Portfolio(balance = initial_balance)
        self.Data = dt.Data()

        while True:
            run = input('Check stock price[S], check portfolio[P] or place order[O]?')
            if run == 'S':
                choice1 = input('[price/plot]?')
                self.Data.get_data()
                if choice1 == 'price':
                    print('current price equals '+str(self.Data.get_summary(type= choice1)))
                elif choice1 == 'plot':
                    self.Data.get_summary(type=choice1)

            elif run == 'P':
                choice2 = input('Check balance[B] or stock portfolio [P]?')
                if choice2 == 'B':
                    print('balance equals :'+str(self.Portfolio.get_balance()))
                elif choice2 == 'P':
                    print(self.Portfolio.get_stocks())
                else:
                    print("That's not a valid command")

            elif run == 'O':
                print('please specify order')
                order_type = input('what is the order type: [Buy/Sell]')
            elif run == 'exit':
                break



