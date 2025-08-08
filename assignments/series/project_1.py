import numpy as np

def main():
    sales = [x for x in range(1, 11)]
    arr = np.array(sales)

    print(f"Dimensions: {arr.ndim}")
    print(f"Size of dimension: {arr.shape}")
    print(f"Size of array: {arr.size}")
    print(f"Data type: {arr.dtype}")


if __name__ == "__main__":
    main()