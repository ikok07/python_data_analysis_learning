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

    transactions_df = transactions_df.assign(
        target_pct=transactions_df["transactions"] / 2500,
        met_target=(transactions_df["transactions"] / 2500) >= 1,
        bonus_payable=((transactions_df["transactions"] / 2500) >= 1) * 100,
        week=transactions_df["date"].dt.isocalendar().week,
        day_of_week=transactions_df["date"].dt.day_of_week,
    )

    transactions_df = transactions_df.assign(store_avg_trans=transactions_df.groupby(["store_nbr", "day_of_week"])["transactions"].transform("mean"))
    transactions_df = transactions_df.assign(trans_vs_avg=transactions_df["transactions"] - transactions_df["store_avg_trans"])

    print(transactions_df)

if __name__ == "__main__":
    main()