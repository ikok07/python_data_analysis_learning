import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    description = transactions_df.describe(include="all")

    print("----- SAMPLES -----")
    print(transactions_df.head(5))

    print("----- INFO -----")
    print(transactions_df.info())

    print("----- STATS -----")
    print(f"Unique dates: {description["date"]["unique"]}")
    print(f"Mean: {description["transactions"]["mean"]}")
    print(f"Median: {transactions_df["transactions"].median()}")
    print(f"Min: {description["transactions"]["min"]}")
    print(f"Max: {description["transactions"]["max"]}")

if __name__ == "__main__":
    main()