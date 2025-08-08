import numpy as np
import pandas as pd

def buy(price, limit):
   if price < limit:
      return "buy"
   return "wait"


def main():
   oil_data = pd.read_csv("data/oil.csv").dropna()
   oil_dates = oil_data["date"].iloc[1000:1100]
   oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
   oil_prices.index = oil_dates

   print(oil_prices.apply(lambda x: "Buy" if x < oil_prices.quantile(.9) else "Wait"))

   updated_prices = pd.Series(np.where(oil_prices.index.isin(["2016-12-23", "2017-05-10"]), oil_prices * 0.9, oil_prices * 1.1), index=oil_dates)
   print(updated_prices)
   pass

if __name__ == "__main__":
    main()