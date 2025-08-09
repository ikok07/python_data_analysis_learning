import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    highest_transactions_df = transactions_df.sort_values("transactions", ascending=False).head(5)
    print(highest_transactions_df)
    print(
        transactions_df.sort_values(
            ["date", "transactions"],
            ascending=[True, False]
        )[transactions_df.columns.sort_values(ascending=False)]
    )


if __name__ == "__main__":
    main()