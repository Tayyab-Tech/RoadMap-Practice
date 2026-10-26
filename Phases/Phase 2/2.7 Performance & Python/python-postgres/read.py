from database import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    SELECT product_id, name, price, category, stock
    FROM products
    ORDER BY product_id
""")

products = cursor.fetchall()

for product in products:
    print(product)

cursor.close()
conn.close()