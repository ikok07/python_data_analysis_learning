import pandas as pd

def main():
    oil_data = pd.read_csv("data/oil.csv")
    oil_prices = pd.Series(oil_data["dcoilwtico"].iloc[1000:1100], name="Oil Prices")
    print(oil_prices)
    print(f"Index: {oil_prices.index}")
    print(f"Name: {oil_prices.name}")
    print(f"Size: {oil_prices.size}")
    print(f"Data type: {oil_prices.dtype}")
    print(f"Mean: {oil_prices.mean()}")

if __name__ == "__main__":
    main()