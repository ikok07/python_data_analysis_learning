import time

import numpy as np

def main():
    rng = np.random.default_rng(2022)
    randomNums = rng.random(9, dtype="float64").reshape(3, 3)

    print(f"Original array:\n {randomNums}")
    print(f"First two rows:\n {randomNums[:2]}")
    print(f"First column:\n {randomNums[:, 0].reshape(3, 1)}")
    print(f"Second number in the third row:\n {randomNums[2, 1]}")


if __name__ == "__main__":
    main()