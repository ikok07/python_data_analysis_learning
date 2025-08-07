import numpy as np
import pandas as pd

def main():
   oil_data = pd.read_csv("data/oil.csv").dropna()
   oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
   oil_prices.index = oil_data["date"].iloc[1000:1100]

   target_dates = [
       "2016-12-22",
       "2017-05-03",
       "2017-01-06",
       "2017-03-05",
       "2017-02-12",
       "2017-03-21",
       "2017-04-14",
       "2017-04-15",
   ]

   lowest_prices = oil_prices.sort_values().iloc[:10].sort_index(ascending=False)
   filtered_prices = oil_prices[(oil_prices.index.isin(target_dates)) & (oil_prices <= 50)]

if __name__ == "__main__":
    main()