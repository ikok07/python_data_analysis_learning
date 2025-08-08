import time

import numpy as np

def main():
    rnd = np.random.default_rng(2022)
    prices = np.array([5.99, 6.99, 22.99, 99.99, 4.99, 49.99])
    discounts = rnd.random(len(prices))

    totalAmount = ((prices + 5) * (1 - discounts)).round(2)
    print(totalAmount)

if __name__ == "__main__":
    main()