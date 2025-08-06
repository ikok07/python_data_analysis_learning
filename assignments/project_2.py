import time

import numpy as np

def main():
    sales = np.linspace(10, 100, 10).reshape(5, 2)
    rng = np.random.default_rng(round(time.time()))
    randomNums = rng.random(9, dtype="float64").reshape(3, 3).round()

    print(sales)
    print(randomNums)
    print(sales[0:5:2])

if __name__ == "__main__":
    main()