import unittest
from CTG import data

class TestData(unittest.TestCase):
    def test_total_price(self):
        p = Product("testproduct", 10)
        o = Order(p,1)
        self.assertEqual(10, o.total_price())

    def test_create_empty_order(self):
        # Try to create an order with 0 products
        # test that you get an error
        p = Product("goodproduct", 5)
        #o = Order(p,0)
        self.assertRaises(ValueError, Order, p, 0)
        #self.assertNotEqual(o.total_price(), 0)
