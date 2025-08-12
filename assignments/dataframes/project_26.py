import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    transactions_df = transactions_df.assign(
        date=transactions_df["date"].astype("datetime64[s]"),
        store_nbr=transactions_df["store_nbr"].astype("int8"),
        transactions=transactions_df["transactions"].astype("int16")
    )
    transactions_df["month"] = transactions_df["date"].dt.month

    top10_stores = transactions_df.groupby(["store_nbr", "month"])[["transactions"]].sum().sort_values(["month", "transactions"], ascending=[True, False])
    print(top10_stores)



if __name__ == "__main__":
    main()