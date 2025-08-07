import numpy as np
import pandas as pd

def main():
   oil_data = pd.read_csv("data/oil.csv").dropna()
   oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
   oil_prices.index = oil_data["date"].iloc[1000:1100]

   higher_prices = oil_prices * 1.1 + 2
   max_price = oil_prices.max()
   prices_difference = pd.Series((oil_prices - max_price)/max_price)

   months = pd.Series(oil_prices.index.str.split("-").str[1].astype("int"))

if __name__ == "__main__":
    main()