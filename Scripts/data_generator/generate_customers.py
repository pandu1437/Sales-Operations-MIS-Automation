import random
from faker import Faker
import pandas as pd

from config import CUSTOMER_FILE, NUM_CUSTOMERS

fake = Faker("en_IN")
random.seed(42)


def generate_customers():

    customers = []

    cities = [
        ("Hyderabad", "Telangana"),
        ("Bengaluru", "Karnataka"),
        ("Chennai", "Tamil Nadu"),
        ("Mumbai", "Maharashtra"),
        ("Pune", "Maharashtra"),
        ("Delhi", "Delhi"),
        ("Kolkata", "West Bengal"),
        ("Vijayawada", "Andhra Pradesh"),
        ("Visakhapatnam", "Andhra Pradesh"),
        ("Kochi", "Kerala"),
    ]

    for customer_id in range(10001, 10001 + NUM_CUSTOMERS):

        city, state = random.choice(cities)

        customers.append([
            customer_id,
            fake.name(),
            random.choice(["Male", "Female"]),
            fake.phone_number(),
            city,
            state,
            fake.email(),
        ])

    df = pd.DataFrame(
        customers,
        columns=[
            "CustomerID",
            "CustomerName",
            "Gender",
            "Phone",
            "City",
            "State",
            "Email",
        ],
    )

    df.to_csv(CUSTOMER_FILE, index=False)

    print("✅ Customers Created Successfully")
    print(df.head())

    return df


if __name__ == "__main__":
    generate_customers()