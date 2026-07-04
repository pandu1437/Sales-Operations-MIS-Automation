import pandas as pd

from config import BRANCH_FILE

def generate_branches():
    branches = [
        [1, "HYD001", "Hyderabad Central", "Hyderabad", "Telangana", "South", "Ramesh Kumar"],
        [2, "BLR001", "Bengaluru Tech Park", "Bengaluru", "Karnataka", "South", "Priya Sharma"],
        [3, "CHE001", "Chennai Express", "Chennai", "Tamil Nadu", "South", "Arun Raj"],
        [4, "VJA001", "Vijayawada One", "Vijayawada", "Andhra Pradesh", "South", "Sneha Reddy"],
        [5, "VSK001", "Vizag Beach Road", "Visakhapatnam", "Andhra Pradesh", "South", "Vikram Rao"],
        [6, "MUM001", "Mumbai Andheri", "Mumbai", "Maharashtra", "West", "Neha Gupta"],
        [7, "DEL001", "Delhi Connaught", "New Delhi", "Delhi", "North", "Rahul Mehta"],
        [8, "PUN001", "Pune City", "Pune", "Maharashtra", "West", "Amit Joshi"],
        [9, "KOL001", "Kolkata Central", "Kolkata", "West Bengal", "East", "Sourav Das"],
        [10, "JAI001", "Jaipur Pink City", "Jaipur", "Rajasthan", "North", "Pooja Singh"],
        [11, "AHM001", "Ahmedabad CG Road", "Ahmedabad", "Gujarat", "West", "Nitin Patel"],
        [12, "LKO001", "Lucknow Metro", "Lucknow", "Uttar Pradesh", "North", "Anjali Verma"],
        [13, "KOC001", "Kochi Marine", "Kochi", "Kerala", "South", "Joseph Mathew"],
        [14, "CBE001", "Coimbatore Hub", "Coimbatore", "Tamil Nadu", "South", "Karthik S"],
        [15, "BPL001", "Bhopal Lake View", "Bhopal", "Madhya Pradesh", "Central", "Deepak Mishra"],
    ]

    columns = [
        "BranchID",
        "BranchCode",
        "BranchName",
        "City",
        "State",
        "Zone",
        "Manager",
    ]

    df = pd.DataFrame(branches, columns=columns)

    df.to_csv(BRANCH_FILE, index=False)

    print(f"✅ Branch dataset created successfully!")
    print(f"📁 File saved to: {BRANCH_FILE}")
    print(f"📊 Total Branches: {len(df)}")

    return df


if __name__ == "__main__":
    generate_branches()