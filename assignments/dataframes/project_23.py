import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    transactions_df["pct_to_target"] = transactions_df["transactions"] / 2500
    transactions_df["met_target"] = transactions_df["pct_to_target"] >= 1
    transactions_df["bonus_playable"] = np.where(transactions_df["met_target"], 100, 0)

    print(f"Bonus playable sum: {transactions_df["bonus_playable"].sum()}")


if __name__ == "__main__":
    main()