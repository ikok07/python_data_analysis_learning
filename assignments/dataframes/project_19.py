import numpy as np
import pandas as pd

def main():
    oil_prices = pd.read_csv("data/oil.csv")
    missing_rows_count = oil_prices[oil_prices["dcoilwtico"].isna()].shape[0]
    print(f"Number of missing prices: {missing_rows_count}")

    print(f"Mean with NaN filled with 0: {oil_prices["dcoilwtico"].fillna(0).mean()}")
    print(f"Mean with NaN filled with mean: {oil_prices["dcoilwtico"].fillna(oil_prices["dcoilwtico"].mean()).mean()}")


if __name__ == "__main__":
    main()