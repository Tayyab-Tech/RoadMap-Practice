from database import get_connection


conn = get_connection()
cursor = conn.cursor()

products = [
    ("Mouse", 2500, "Electronics", 50),
    ("Keyboard", 5000, "Electronics", 30),
    ("Office Chair", 25000, "Furniture", 15),
]

cursor.executemany("""
    INSERT INTO products (name, price, category, stock)
    VALUES (%s, %s, %s, %s)
""", products)

conn.commit()

cursor.close()
conn.close()

print("Products inserted!")