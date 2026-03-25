def load(df):
    print("[LOG] Starting load...")
    df.to_csv("data/output.csv", index=False)
    print("[LOG] Data saved to output.csv")