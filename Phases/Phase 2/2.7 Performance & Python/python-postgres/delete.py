from database import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    DELETE FROM products
    WHERE product_id = %s
""", (1,))

conn.commit()

cursor.close()
conn.close()

print("Product deleted!")