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
        day_of_week=transactions_df["date"].dt.day_of_week
    )

    data_by_store = transactions_df.groupby(["store_nbr"]).agg(met_target_avg=("met_target", "mean"),
                                                               bonus_payable=("bonus_payable", "sum")).sort_values(
        by="bonus_payable", ascending=False)
    data_by_month = transactions_df.groupby(["month"]).agg(met_target_avg=("met_target", "mean"),
                                                           bonus_payable=("bonus_payable", "sum")).sort_values(
        by="bonus_payable", ascending=False)
    data_by_week = transactions_df.groupby(["week"]).agg(met_target_avg=("met_target", "mean"),
                                                         bonus_payable=("bonus_payable", "sum")).sort_values(
        by="bonus_payable", ascending=False)


if __name__ == "__main__":
    main()