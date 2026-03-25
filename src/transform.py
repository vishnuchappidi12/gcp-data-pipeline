def transform(df):
    df["amount"] = df["amount"] * 1.1  # add 10% tax
    print("Data Transformed")
    return df