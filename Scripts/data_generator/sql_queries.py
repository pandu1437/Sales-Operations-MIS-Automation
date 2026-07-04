import sqlite3
import pandas as pd

DB_PATH = r"C:\Users\laksh\OneDrive\Desktop\Sales-Operations-MIS-Automation\SQL\sales_database.db"

conn = sqlite3.connect(DB_PATH)

print("\n📊 TOP 5 SALES RECORDS\n")

df = pd.read_sql("SELECT * FROM sales LIMIT 5", conn)
print(df)

print("\n💰 TOTAL REVENUE\n")

df2 = pd.read_sql("SELECT SUM(FinalAmount) AS TotalRevenue FROM sales", conn)
print(df2)

conn.close()