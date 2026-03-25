def load(df):
    df.to_csv("data/output.csv", index=False)
    print("Data Loaded")