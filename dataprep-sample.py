import google.cloud.bigquery as bq

client = bq.Client()

query = """
SELECT candidate_name, party, total_receipts, total_disbursements
FROM `fec_dataset.candidate_finance`
WHERE election_year = 2016
ORDER BY total_receipts DESC
"""

df = client.query(query).to_dataframe()
df.to_csv("cleaned_fec_data.csv", index=False)
print("Data wrangling complete!")