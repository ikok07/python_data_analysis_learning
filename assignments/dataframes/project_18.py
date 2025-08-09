import numpy as np
import pandas as pd

def main():
    transactions_df = pd.read_csv("data/transactions.csv")

    cleaned_data = transactions_df.drop(index=[0], columns=["date"])
    print(f"Cleaned data:\n{cleaned_data}")

    last_store_data = transactions_df.drop_duplicates(subset="store_nbr", keep="last")
    print(f"Last row for each of stores:\n{last_store_data}")

if __name__ == "__main__":
    main()