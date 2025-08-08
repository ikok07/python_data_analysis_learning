import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")

    print(transactions_df)
    print(f"Rows: {transactions_df.shape[0]}\nColumns: {transactions_df.shape[1]}")
    print(transactions_df.dtypes)

if __name__ == "__main__":
    main()