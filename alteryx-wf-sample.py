import pandas as pd

# Load raw FEC data
df = pd.read_csv("fec_raw_data.csv")

# Clean and filter data
df = df[df["election_year"] == 2016]
df = df[["candidate_name", "party", "total_receipts", "total_disbursements"]]

# Save cleaned data
df.to_csv("fec_cleaned_data.csv", index=False)
print("Alteryx data wrangling complete!")