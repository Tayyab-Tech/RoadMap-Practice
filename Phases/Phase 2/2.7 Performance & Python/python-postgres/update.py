from database import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    UPDATE products
    SET price = %s
    WHERE product_id = %s
""", (145000, 1))

conn.commit()

cursor.close()
conn.close()

print("Product updated!")