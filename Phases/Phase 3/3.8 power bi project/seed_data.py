
import os
import random
from datetime import date, timedelta
from decimal import Decimal

import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
random.seed(42)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing from .env")


CATEGORIES = [
    "Electronics",
    "Home & Kitchen",
    "Fashion",
    "Sports",
    "Books",
    "Beauty",
]

PRODUCTS = [
    ("Wireless Headphones", "Electronics", 8500, 4200),
    ("Smart Watch", "Electronics", 12000, 6500),
    ("Bluetooth Speaker", "Electronics", 5500, 2600),
    ("Laptop Stand", "Electronics", 3500, 1500),
    ("USB-C Hub", "Electronics", 4200, 1900),
    ("Coffee Maker", "Home & Kitchen", 9500, 5100),
    ("Air Fryer", "Home & Kitchen", 18000, 11000),
    ("Water Bottle", "Home & Kitchen", 1800, 600),
    ("Desk Lamp", "Home & Kitchen", 3200, 1400),
    ("Cotton Bedsheet", "Home & Kitchen", 4500, 2500),
    ("Casual T-Shirt", "Fashion", 1800, 700),
    ("Running Shoes", "Fashion", 7500, 4100),
    ("Backpack", "Fashion", 4200, 2000),
    ("Wrist Watch", "Fashion", 6500, 3100),
    ("Yoga Mat", "Sports", 2500, 1000),
    ("Dumbbell Set", "Sports", 6000, 3500),
    ("Football", "Sports", 2200, 900),
    ("Python Programming Book", "Books", 2800, 1300),
    ("Data Analytics Guide", "Books", 3500, 1600),
    ("Face Moisturizer", "Beauty", 1600, 650),
    ("Sunscreen SPF 50", "Beauty", 2200, 950),
    ("Hair Dryer", "Beauty", 4800, 2500),
]

CITIES = [
    ("Lahore", "Punjab"),
    ("Karachi", "Sindh"),
    ("Islamabad", "Islamabad Capital Territory"),
    ("Rawalpindi", "Punjab"),
    ("Faisalabad", "Punjab"),
    ("Multan", "Punjab"),
    ("Peshawar", "Khyber Pakhtunkhwa"),
    ("Quetta", "Balochistan"),
]

FIRST_NAMES = [
    "Ali", "Ahmed", "Sara", "Ayesha", "Usman",
    "Fatima", "Hamza", "Zain", "Hira", "Bilal",
    "Maryam", "Saad", "Noor", "Hassan", "Amna",
    "Umar", "Zoya", "Daniyal", "Maham", "Ibrahim",
]

LAST_NAMES = [
    "Khan", "Ahmed", "Malik", "Sheikh", "Raza",
    "Hussain", "Iqbal", "Butt", "Chaudhry", "Siddiqui",
]

START_DATE = date(2025, 1, 1)
END_DATE = date(2026, 10, 1)


def random_date(start, end):
    days = (end - start).days
    return start + timedelta(days=random.randint(0, days))


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def create_schema(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(100) UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(150) NOT NULL,
            category_id INTEGER NOT NULL
                REFERENCES categories(category_id),
            price NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
            cost NUMERIC(12, 2) NOT NULL CHECK (cost >= 0),
            created_at DATE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(150) NOT NULL,
            email VARCHAR(200) UNIQUE NOT NULL,
            city VARCHAR(100),
            country VARCHAR(100) NOT NULL DEFAULT 'Pakistan',
            signup_date DATE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL
                REFERENCES customers(customer_id),
            order_date DATE NOT NULL,
            order_status VARCHAR(30) NOT NULL
                CHECK (order_status IN (
                    'Delivered', 'Shipped', 'Processing',
                    'Cancelled', 'Returned'
                )),
            shipping_fee NUMERIC(10, 2) NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id SERIAL PRIMARY KEY,
            order_id INTEGER NOT NULL
                REFERENCES orders(order_id),
            product_id INTEGER NOT NULL
                REFERENCES products(product_id),
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            unit_price NUMERIC(12, 2) NOT NULL
                CHECK (unit_price >= 0),
            unit_cost NUMERIC(12, 2) NOT NULL
                CHECK (unit_cost >= 0),
            discount_amount NUMERIC(12, 2) NOT NULL DEFAULT 0
                CHECK (discount_amount >= 0)
        );

        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL
                REFERENCES customers(customer_id),
            product_id INTEGER NOT NULL
                REFERENCES products(product_id),
            order_id INTEGER NOT NULL
                REFERENCES orders(order_id),
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
            review_text TEXT,
            review_date DATE NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_products_category
            ON products(category_id);

        CREATE INDEX IF NOT EXISTS idx_orders_customer
            ON orders(customer_id);

        CREATE INDEX IF NOT EXISTS idx_orders_date
            ON orders(order_date);

        CREATE INDEX IF NOT EXISTS idx_order_items_order
            ON order_items(order_id);

        CREATE INDEX IF NOT EXISTS idx_order_items_product
            ON order_items(product_id);

        CREATE INDEX IF NOT EXISTS idx_reviews_product
            ON reviews(product_id);
    """)


def seed_database():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            create_schema(cur)

            # Avoid duplicating the sample dataset on reruns.
            cur.execute("SELECT COUNT(*) FROM orders")
            existing_orders = cur.fetchone()[0]

            if existing_orders:
                print(
                    f"Seed skipped: database already has "
                    f"{existing_orders} orders."
                )
                print("Existing records were not modified.")
                return

            # 1. Categories
            category_ids = {}

            for category in CATEGORIES:
                cur.execute("""
                    INSERT INTO categories (category_name)
                    VALUES (%s)
                    RETURNING category_id
                """, (category,))

                category_ids[category] = cur.fetchone()[0]

            # 2. Products
            product_data = {}

            for name, category, price, cost in PRODUCTS:
                created_at = random_date(
                    date(2024, 1, 1), START_DATE
                )

                cur.execute("""
                    INSERT INTO products (
                        product_name, category_id, price,
                        cost, created_at
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING product_id
                """, (
                    name,
                    category_ids[category],
                    money(price),
                    money(cost),
                    created_at,
                ))

                product_id = cur.fetchone()[0]

                product_data[product_id] = {
                    "name": name,
                    "price": price,
                    "cost": cost,
                }

            # 3. Customers
            customer_ids = []

            for i in range(60):
                first = random.choice(FIRST_NAMES)
                last = random.choice(LAST_NAMES)
                city, region = random.choice(CITIES)

                cur.execute("""
                    INSERT INTO customers (
                        customer_name, email, city,
                        country, signup_date
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING customer_id
                """, (
                    f"{first} {last}",
                    f"customer{i + 1:03d}@example.com",
                    city,
                    "Pakistan",
                    random_date(
                        date(2024, 1, 1), END_DATE
                    ),
                ))

                customer_ids.append(cur.fetchone()[0])

            # 4. Orders and 5. Order items
            order_statuses = [
                "Delivered", "Delivered", "Delivered",
                "Shipped", "Processing", "Cancelled", "Returned"
            ]

            order_ids = []
            purchased_items = []

            for _ in range(250):
                customer_id = random.choice(customer_ids)
                order_date = random_date(START_DATE, END_DATE)
                status = random.choice(order_statuses)
                shipping_fee = random.choice([0, 150, 200, 250, 300])

                cur.execute("""
                    INSERT INTO orders (
                        customer_id, order_date,
                        order_status, shipping_fee
                    )
                    VALUES (%s, %s, %s, %s)
                    RETURNING order_id
                """, (
                    customer_id,
                    order_date,
                    status,
                    money(shipping_fee),
                ))

                order_id = cur.fetchone()[0]
                order_ids.append(order_id)

                selected_products = random.sample(
                    list(product_data.keys()),
                    random.randint(1, 4)
                )

                for product_id in selected_products:
                    product = product_data[product_id]
                    quantity = random.randint(1, 4)
                    unit_price = money(product["price"])
                    unit_cost = money(product["cost"])

                    # Discount is per order-item line.
                    gross = unit_price * quantity
                    discount = money(
                        gross * Decimal(
                            str(random.choice([0, 0, 0.05, 0.10, 0.15]))
                        )
                    )

                    cur.execute("""
                        INSERT INTO order_items (
                            order_id, product_id, quantity,
                            unit_price, unit_cost, discount_amount
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING order_item_id
                    """, (
                        order_id,
                        product_id,
                        quantity,
                        unit_price,
                        unit_cost,
                        discount,
                    ))

                    item_id = cur.fetchone()[0]

                    purchased_items.append({
                        "order_id": order_id,
                        "customer_id": customer_id,
                        "product_id": product_id,
                        "order_date": order_date,
                        "order_item_id": item_id,
                    })

            # 6. Reviews, linked to a real purchased product.
            review_texts = [
                "Excellent quality.",
                "Good value for money.",
                "Works as expected.",
                "Delivery was a little slow.",
                "Could be improved.",
                "Very satisfied with this purchase.",
                "Average product.",
            ]

            reviewed = set()

            for item in purchased_items:
                if random.random() > 0.30:
                    continue

                key = (item["order_id"], item["product_id"])

                if key in reviewed:
                    continue

                reviewed.add(key)

                cur.execute("""
                    INSERT INTO reviews (
                        customer_id, product_id, order_id,
                        rating, review_text, review_date
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    item["customer_id"],
                    item["product_id"],
                    item["order_id"],
                    random.randint(1, 5),
                    random.choice(review_texts),
                    item["order_date"],
                ))

            # The connection context commits on success
            # and rolls back if an exception occurs.

    print("Neon e-commerce database seeded successfully!")


if __name__ == "__main__":
    seed_database()
