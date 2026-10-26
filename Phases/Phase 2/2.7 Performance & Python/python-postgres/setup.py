from database import get_connection


conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price NUMERIC(10, 2) NOT NULL,
        category VARCHAR(50),
        stock INTEGER DEFAULT 0
    )
""")

conn.commit()

cursor.close()
conn.close()

print("Products table created successfully!")