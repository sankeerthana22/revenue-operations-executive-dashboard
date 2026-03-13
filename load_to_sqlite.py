import pandas as pd
import sqlite3
import os

DB_PATH = "revenue_ops.db"
RAW_PATH = "data/raw"

files = {
    "sales_reps": "sales_reps.csv",
    "campaigns": "campaigns.csv",
    "leads": "leads.csv",
    "customers": "customers.csv",
    "orders": "orders.csv",
    "targets": "targets.csv"
}

conn = sqlite3.connect(DB_PATH)

for table_name, file_name in files.items():
    file_path = os.path.join(RAW_PATH, file_name)
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {table_name}: {len(df)} rows")

conn.close()
print(f"\nSQLite database created successfully at: {DB_PATH}")
