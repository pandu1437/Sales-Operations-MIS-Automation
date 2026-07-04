import random
import pandas as pd
from faker import Faker

from config import (
    SALES_FILE,
    CUSTOMER_FILE,
    EMPLOYEE_FILE,
    PRODUCT_FILE,
    BRANCH_FILE,
    NUM_SALES,
)

fake = Faker("en_IN")
random.seed(42)


def calculate_amount(quantity, unit_price, discount_percent):

    gst_percent = 18

    gross_amount = quantity * unit_price
    discount_amount = gross_amount * (discount_percent / 100)
    taxable_amount = gross_amount - discount_amount
    gst_amount = taxable_amount * (gst_percent / 100)
    final_amount = taxable_amount + gst_amount

    return gross_amount, discount_amount, taxable_amount, gst_amount, final_amount, gst_percent


def generate_sales():

    print("🚀 STARTED SALES GENERATION")

    customers = pd.read_csv(CUSTOMER_FILE)
    employees = pd.read_csv(EMPLOYEE_FILE)
    products = pd.read_csv(PRODUCT_FILE)
    branches = pd.read_csv(BRANCH_FILE)

    print(f"Customers : {len(customers)}")
    print(f"Employees : {len(employees)}")
    print(f"Products  : {len(products)}")
    print(f"Branches  : {len(branches)}")

    sales = []

    for i in range(1, NUM_SALES + 1):

        customer = customers.sample(1).iloc[0]
        employee = employees.sample(1).iloc[0]
        product = products.sample(1).iloc[0]

        quantity = random.randint(1, 5)
        unit_price = product["SellingPrice"]
        discount_percent = random.choice([0, 5, 10, 15])

        gross_amount, discount_amount, taxable_amount, gst_amount, final_amount, gst_percent = calculate_amount(
            quantity, unit_price, discount_percent
        )

        sales.append([
            f"S{100000 + i}",
            fake.date_between(start_date="-2y", end_date="today"),
            customer["CustomerID"],
            employee["EmployeeID"],
            employee["BranchID"],
            product["ProductID"],
            quantity,
            unit_price,
            discount_percent,
            gst_percent,
            round(gross_amount, 2),
            round(discount_amount, 2),
            round(taxable_amount, 2),
            round(gst_amount, 2),
            round(final_amount, 2),
        ])

    print(f"Generated {len(sales)} records")

    columns = [
        "SalesID",
        "OrderDate",
        "CustomerID",
        "EmployeeID",
        "BranchID",
        "ProductID",
        "Quantity",
        "UnitPrice",
        "DiscountPercent",
        "GSTPercent",
        "GrossAmount",
        "DiscountAmount",
        "TaxableAmount",
        "GSTAmount",
        "FinalAmount",
    ]

    df = pd.DataFrame(sales, columns=columns)

    df.to_csv(SALES_FILE, index=False)

    print("✅ SALES FILE CREATED")
    print("📁 Location:", SALES_FILE)
    print(df.head())


if __name__ == "__main__":
    generate_sales()