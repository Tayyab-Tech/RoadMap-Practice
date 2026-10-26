from database import get_connection


def get_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM products
        ORDER BY product_id
    """)

    products = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return products
