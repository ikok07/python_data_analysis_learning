import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    transactions_df["date"] = pd.to_datetime(transactions_df["date"])
    bonus_conditions = [transactions_df["date"].dt.month == 12, (transactions_df["date"].dt.day_of_week == 6) & (transactions_df["date"].dt.month == 5), (transactions_df["date"].dt.day_of_week == 0) & (transactions_df["date"].dt.month == 7)]
    bonus_names = ["Holiday Bonus", "Corporate Month", "Summer Special"]

    transactions_df["seasonal_bonus"] = np.select(bonus_conditions, bonus_names, default="None")

    print(f"Total bonus owned: {transactions_df[transactions_df["seasonal_bonus"] != "None"]["seasonal_bonus"].value_counts().sum() * 100}")

if __name__ == "__main__":
    main()