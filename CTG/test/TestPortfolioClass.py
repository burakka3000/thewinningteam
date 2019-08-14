import unittest
import CTG.CTG.Portfolio as pt
import CTG.CTG.data as dt
import pandas as pd

class TestPortfolio(unittest.TestCase):
    def test_get_stock_value(self):
        # Test whether stock value is correctly returned
        data = dt.Data()
        data.get_data()
        p = pt.Portfolio(data = data, balance = 1000)
        p.update_stocks('AAPL',2)

        self.assertEqual(p.get_stock_value(), 2*data.summary.loc[data.summary['Ticker']=='AAPL','Price'].values)

if __name__ == '__main__':
    unittest.main()
