import CTG.CTG.Portfolio as pf
import CTG.CTG.data as dt

class Interface:
    def __init__(self, initial_balance):
        self.Portfolio = pf.Portfolio(balance = initial_balance)
        self.Data = dt.Data()
        self.run = True

        while run:
            run = input('Check stock price[S], check portfolio[P] or place order[O]?')
            if run == 'S':
                print(self.Data.get_summary)

            elif run == 'P':
                choice2 = input('Check balance[B] or stock portfolio [P]?')
                if choice2 == 'B':
                    print('balance equals :'+self.Portfolio.get_balance())
                if choice2 == 'P':
                    print(self.Portfolio.get_stocks())
                else:
                    print("That's not a valid command")

            elif run == 'O':
                print('please specify order')
                order_type = input('what is the order type: [Buy/Sell]')
                
            run = ""
        else:
            print('Thats not a valid command')

