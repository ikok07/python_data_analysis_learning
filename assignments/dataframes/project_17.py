import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")

    filtered_data = transactions_df.loc[1:, ["store_nbr", "transactions"]]
    print("------ FILTERED DATA ------")
    print(filtered_data)

    print("------ STATS ------")
    print(f"Unique store numbers:\n {filtered_data["store_nbr"].nunique()}")
    print(f"Total transactions (in millions):\n {filtered_data["transactions"].sum() / 1_000_000}")

if __name__ == "__main__":
    main()