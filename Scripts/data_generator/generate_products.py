import random
import pandas as pd

from config import PRODUCT_FILE

random.seed(42)


def generate_products():

    products = []

    product_id = 1001

    catalog = {

        "Laptop": [

            ("Dell", "Inspiron 15"),
            ("Dell", "XPS 13"),
            ("HP", "Pavilion"),
            ("HP", "Victus"),
            ("Lenovo", "IdeaPad Slim"),
            ("Lenovo", "ThinkPad E14"),
            ("Asus", "Vivobook 15"),
            ("Asus", "ROG Strix"),
            ("Acer", "Aspire 7"),
            ("Apple", "MacBook Air")

        ],

        "Mobile": [

            ("Apple", "iPhone 16"),
            ("Samsung", "Galaxy S25"),
            ("Samsung", "Galaxy A56"),
            ("OnePlus", "OnePlus 13"),
            ("Xiaomi", "Redmi Note 15"),
            ("Realme", "Realme GT"),
            ("Vivo", "Vivo V50"),
            ("Oppo", "Reno 14"),
            ("Nothing", "Phone 3"),
            ("Motorola", "Edge 60")

        ],

        "Tablet": [

            ("Apple", "iPad Air"),
            ("Samsung", "Galaxy Tab S10"),
            ("Lenovo", "Tab P12"),
            ("Xiaomi", "Pad 7"),
            ("Honor", "Pad X9")

        ],

        "Accessory": [

            ("Logitech", "Wireless Mouse"),
            ("Logitech", "Mechanical Keyboard"),
            ("Boat", "Airdopes"),
            ("Sony", "WH-1000XM6"),
            ("JBL", "Flip Speaker"),
            ("HP", "Laptop Backpack"),
            ("Dell", "USB-C Dock"),
            ("Apple", "MagSafe Charger"),
            ("Samsung", "45W Charger"),
            ("Anker", "Power Bank")

        ]

    }

    for category, items in catalog.items():

        for brand, model in items:

            cost = random.randint(500, 80000)

            selling = int(cost * random.uniform(1.15, 1.35))

            stock = random.randint(20, 250)

            products.append([

                product_id,
                brand,
                model,
                category,
                cost,
                selling,
                stock

            ])

            product_id += 1

    df = pd.DataFrame(

        products,

        columns=[

            "ProductID",
            "Brand",
            "ProductName",
            "Category",
            "CostPrice",
            "SellingPrice",
            "Stock"

        ]

    )

    df.to_csv(PRODUCT_FILE, index=False)

    print("✅ Products Created Successfully")
    print(df.head())

    return df


if __name__ == "__main__":
    generate_products()