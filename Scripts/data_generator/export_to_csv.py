import sqlite3
import pandas as pd

DB_PATH = r"C:\Users\laksh\OneDrive\Desktop\Sales-Operations-MIS-Automation\SQL\sales_database.db"
OUTPUT_PATH = r"C:\Users\laksh\OneDrive\Desktop\Sales-Operations-MIS-Automation\Data\sales_export.csv"

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql("SELECT * FROM sales", conn)

df.to_csv(OUTPUT_PATH, index=False)

conn.close()

print("✅ CSV exported successfully!")