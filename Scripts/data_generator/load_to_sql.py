import os
import pandas as pd
import sqlite3
from config import SALES_FILE


def load_data():

    print("🚀 Loading CSV file...")

    # Read CSV
    df = pd.read_csv(SALES_FILE)

    print("Rows:", df.shape)

    # Find project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Create SQL folder
    sql_dir = os.path.join(base_dir, "SQL")
    os.makedirs(sql_dir, exist_ok=True)

    # Database path
    db_path = os.path.join(sql_dir, "sales_database.db")

    # Connect to SQLite
    conn = sqlite3.connect(db_path)

    # Load data into SQL
    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Data loaded successfully!")
    print("📁 Database saved at:", db_path)


if __name__ == "__main__":
    load_data()