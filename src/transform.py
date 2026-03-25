def transform(df):
    print("[LOG] Starting transformation...")
    df["amount"] = df["amount"] * 1.1
    print("[LOG] Transformation completed")
    return df