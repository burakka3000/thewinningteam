import numpy as np
import matplotlib as plt
import pandas as pd
import requests


class Data():

    def __init__(self):
        pass

    def __str__(self):
        print("Your data get extracted from here") #string representation of this class

    def get_data(self):
        response = requests.get(
            "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")
        # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
        # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        if response.status_code != 200:
            raise ValueError("Could not retrieve data, code:", response.status_code)

        # The service sends JSON data, we parse that into a Python datastructure
        raw_data = response.json()
        df = pd.DataFrame.from_dict(raw_data['Time Series (5min)']).T #this line puts the time series values of the stokc in a df
        if df.isnull().values.any() == True:
            df.fillna(method='ffill') #fill na values if there are any
        self._data = df #make the df private and accessible within the class (for other methods)

    def get_summary(self, type='price'):
        self.type = type

        if self.type == 'price':
            price = pd.to_numeric(self._data['4. close'])[0]
            print(price)
        elif self.type == 'plot':
            pd.to_numeric(self._data['4. close']).plot()


