import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    more_than_2000_transactions_count = (transactions_df["transactions"] > 2000).mean()
    print(
        f"Percentage of times all stores had more than 2000 transactions "
        f"{more_than_2000_transactions_count}"
    )

    store25_df = transactions_df.loc[transactions_df["store_nbr"] == 25]
    store25_more_than_2000_transactions = store25_df.loc[store25_df["transactions"] > 2000]
    print(
        f"Percentage of times store 25 had more than 2000 transactions "
        f"{store25_more_than_2000_transactions.shape[0] / store25_df.shape[0]}"
    )
    print(f"Sum of transactions of store 25 over 2000: {store25_more_than_2000_transactions["transactions"].sum()}")

    store25_31_under_2000_transactions_df = transactions_df.loc[
        (transactions_df["store_nbr"].astype("int").isin([25, 31])) &
        (transactions_df["transactions"] < 2000) &
        ((transactions_df["date"].str.contains("-05-")) |
        (transactions_df["date"].str.contains("-06-")))
    ]
    print(store25_31_under_2000_transactions_df["transactions"].sum())

if __name__ == "__main__":
    main()