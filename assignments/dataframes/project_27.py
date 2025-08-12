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

    grouped = (transactions_df.groupby(["store_nbr", "month"]).agg({"transactions": ["sum", "mean"]}).sort_values(["month", ("transactions", "sum")], ascending=[True, False]))
    print(grouped)
    print(f"Store 3, Month 1:\n{grouped.loc[(3, 1)]}")
    print(f"Mean:\n{grouped.loc[:, [("transactions", "mean")]]}")

    grouped.droplevel(0, axis=1).reset_index()
    print(grouped)



if __name__ == "__main__":
    main()