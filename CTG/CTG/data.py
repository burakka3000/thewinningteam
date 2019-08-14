import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from datetime import date, datetime


class Data():

    def __init__(self):
        pass

    def __str__(self):
        print("Your data is being extracted from here") #string representation of this class

    def get_data(self):

        today = date.today()

        try:
            summary_df = pd.read_csv("stock-data-"+str(today).split("-")[2]+"-"+str(today).split("-")[1]+".csv", sep=",", index_col='Unnamed: 0')
            self._summary = summary_df

        except:
            #the ticker symbols for the stocks in our stockmarket
            stocks = ['AAPL', 'MSFT', 'WFC', 'JNJ', 'DIS']
            dic_of_dfs = {}
            summary = {}

            for stock in stocks: #for loop to fetch data for all five stocks in our stockmarket

                response = requests.get(
                    "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+stock+"&interval=5min&outputsize=full&apikey=9JIMZ4CS31GW2257")
                # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
                # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
                if response.status_code != 200:
                    raise ValueError("Could not retrieve data, code:", response.status_code)
                # The service sends JSON data, we parse that into a Python datastructure
                raw_data = response.json()
                df = pd.DataFrame.from_dict(raw_data['Time Series (5min)']).T #this line puts the time series values of the stokc in a df
                if df.isnull().values.any() == True:
                    df.fillna(method='ffill') #fill na values if there are any
                dic_of_dfs[stock] = df #put the dataframe for every stock in this dictionary for every iteration of the loop

                summary[stock] = pd.to_numeric(dic_of_dfs[stock]['4. close'][0])

            summary_df = pd.DataFrame(list(summary.items()), columns=['Ticker', 'Price'])
            summary_df.to_csv("stock-data-"+str(today).split("-")[2]+"-"+str(today).split("-")[1]+".csv", sep=",")

            self._data = dic_of_dfs #make the dict private and accessible within the class (for other methods)
            summary_df['Timestamp'] = datetime.now()
            self._summary = summary_df

    @property
    def summary(self):
        return self._summary # this method returns to the interface the table of latest price values

    def update(self):
        current_time = datetime.now()
        #delta_time = self._summary['Timestamp'] - current_time
        delta_time = current_time - self._summary['Timestamp'][0]
        delta_time /= np.timedelta64(1, 's')
        shocks = np.random.standard_normal(5)
        shocks *= (((delta_time/60))**0.5)*0.01

        for i in range(len(shocks)):
            self.summary["Price"][i] *= np.exp(shocks[i])
            self.summary['Timestamp'][i] = current_time
            # summary_df["Price"][i] *= np.exp(shocks[i])
            # summary_df['Timestamp'][i] = current_time