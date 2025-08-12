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

    pivot = transactions_df[transactions_df["bonus_payable"] > 0].pivot_table(
        index="store_nbr",
        columns="day_of_week",
        values="bonus_payable",
        aggfunc="sum",
        margins=True
    )

    unpivot = pivot.reset_index().melt(
        id_vars="store_nbr",
        value_vars=[0, 1, 2, 3, 4, 5, 6],
        var_name="day_of_week",
        value_name="Total bonuses"
    )

    print(unpivot)

if __name__ == "__main__":
    main()