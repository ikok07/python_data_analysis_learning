import numpy as np
import pandas as pd

def main():
   oil_data = pd.read_csv("data/oil.csv").dropna()
   oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
   oil_prices.index = oil_data["date"].iloc[1000:1100]

   march_prices = oil_prices[oil_prices.index.str.split("-").str[1].astype("int") == 3]
   print(f"March prices sum : {round(march_prices.sum(), 2)}")
   print(f"March prices mean: {round(march_prices.mean(), 2)}")

   print("10th and 90th percentiles:")
   print(oil_prices.quantile([0.1, 0.9]))

   print(f"Number of integer prices: {oil_prices.astype("int").value_counts(normalize=True)}")


if __name__ == "__main__":
    main()