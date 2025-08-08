import time

import numpy as np

def main():
    rnd = np.random.default_rng(2022)

    products = np.array(["product 1", "product 2", "product 3", "product 4", "product 5", "product 6"])
    prices = np.array([5.99, 6.99, 22.49, 99.99, 4.99, 49.99])
    shipping_cost = np.where(prices > 20, 0, 5)
    most_expensive = np.sort(prices)[-3:]

    print(f"Mean: {most_expensive.mean()}")
    print(f"Minimum price: {most_expensive.min()}")
    print(f"<aximum price: {most_expensive.max()}")
    print(f"Median: {np.median(most_expensive)}")
    print(f"Number of unique price tiers: {np.unique(prices).size}")

if __name__ == "__main__":
    main()