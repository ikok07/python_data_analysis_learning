import numpy as np
import pandas as pd

def main():
   oil_data = pd.read_csv("data/oil.csv").dropna()
   oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
   oil_prices.index = oil_data["date"].iloc[1000:1100]

   oil_prices = oil_prices.where(~oil_prices.isin([51.44, 47.83]), np.nan)

   print(f"Missing values count: {oil_prices[oil_prices.isna()].value_counts(dropna=False).values[0]}")

   oil_prices = oil_prices.fillna(oil_prices.median())
   print(oil_prices)

if __name__ == "__main__":
    main()