import pandas as pd

def extract():
    df = pd.read_csv("data/sales.csv")
    print("Data Extracted")
    return df