import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")
    transactions_df.columns = ["date", "store_number", "transaction_count"]
    transactions_df = transactions_df.reindex(columns=["date", "transaction_count", "store_number"])
    print(transactions_df)


if __name__ == "__main__":
    main()