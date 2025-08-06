import numpy as np
import pandas as pd

def main():
    retail_df = pd.read_csv("data/retail_2016_2017.csv", skiprows=range(1, 11000), nrows=1000)
    print(retail_df)

    sales_array = np.array(retail_df["sales"])
    family_array = np.array(retail_df["family"])
    filtered_sales = sales_array[family_array == "PRODUCE"]

    rnd = np.random.default_rng(2022)
    half_filtered_sales = filtered_sales[rnd.random(len(filtered_sales)) < 0.5]

    mean = half_filtered_sales.mean()
    median = np.median(half_filtered_sales)

    above_both = half_filtered_sales[(half_filtered_sales > mean) & (half_filtered_sales > median)]
    above_median = half_filtered_sales[(half_filtered_sales > median) & (half_filtered_sales < mean)]
    below_both = half_filtered_sales[(half_filtered_sales < mean) & (half_filtered_sales < median)]

    print(f"Mean of half of filtered sales: {mean}")
    print(f"Median of half of filtered sales: {median}")

    print(f"Above mean and median\n\t{above_both}")
    print(f"Above median\n\t{above_median}")
    print(f"Below mean and median\n\t{below_both}")

if __name__ == "__main__":
    main()