import time

import numpy as np
import pandas as pd

def main():
    oil_data = pd.read_csv("data/oil.csv").dropna()

    oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
    oil_prices.index = oil_data["date"].iloc[1000:1100]

    period_prices = oil_prices["2017-01-01" : "2017-01-07"].reset_index(drop=True)

    print(f"Period prices: {period_prices}")
    mean = pd.concat([oil_prices.iloc[:10], oil_prices.iloc[-10:]]).mean()
    print(f"Mean: {round(mean, 2)}")

if __name__ == "__main__":
    main()