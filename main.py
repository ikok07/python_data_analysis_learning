import time

import numpy as np

def main():
    rnd = np.random.default_rng(2022)

    products = np.array(["product 1", "product 2", "product 3", "product 4", "product 5", "product 6"])
    prices = np.array([5.99, 6.99, 22.99, 99.99, 4.99, 49.99])
    shipping_cost = np.where(prices > 20, 0, 5)

if __name__ == "__main__":
    main()