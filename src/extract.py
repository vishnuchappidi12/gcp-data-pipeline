import pandas as pd

def extract():
    print("[LOG] Starting data extraction...")
    df = pd.read_csv("data/sales.csv")
    print("[LOG] Data extraction completed")
    return df