import CTG.CTG.Portfolio as pf

TestPortfolio = pf.Portfolio(balance = 1000)

print(TestPortfolio.get_balance())

print(TestPortfolio.get_stocks())

TestPortfolio.update_balance(-100)

print(TestPortfolio.get_balance())

print(TestPortfolio.get_stocks())

TestPortfolio.update_stocks('AAPL',10)

print(TestPortfolio.get_balance())

print(TestPortfolio.get_stocks())

TestPortfolio.update_stocks('AAPL',-5)

print(TestPortfolio.get_balance())

print(TestPortfolio.get_stocks())