# import psycopg

# conn = psycopg.connect(
#     host="localhost",
#     port=5432,
#     dbname="python_store",
#     user="postgres",
#     password="password"
# )

# print("Database connected successfully!")

# conn.close()



# import psycopg

# conn = psycopg.connect(
#     host="localhost",
#     port=5432,
#     dbname="python_store",
#     user="postgres",
#     password="password"
# )

# cursor = conn.cursor()




# cursor.execute("""
#     SELECT product_id, name, price, category, stock
#     FROM products
# """)

# products = cursor.fetchall()
# for p in product:
#     print(p)




# for 1 record 
# cursor.execute("""
#     SELECT *
#     FROM products
#     WHERE product_id = %s
# """, (2,))

# product = cursor.fetchone()

# print(product)

# for p in product:
#     print(p)






# to insert in table 
# cursor.execute("""
#     INSERT INTO products (name, price, category, stock)
#     VALUES (%s, %s, %s, %s)
# """, ("Headphones", 8000, "Electronics", 20))
# conn.commit()





# to update any record
# cursor.execute("""
#     UPDATE products
#     SET price = %s
#     WHERE product_id = %s
# """, (7500, 5))

# conn.commit()




# to delete any record 
# cursor.execute("""
#     DELETE FROM products
#     WHERE product_id = %s
# """, (5,))

# conn.commit()




# parameterized query
# name = input("Enter name: ")

# cursor.execute("""
#     SELECT *
#     FROM products
#     WHERE name = %s
# """, (name,))
# product = cursor.fetchone()
# print(product)






# transaction and roll back
# try:
#     cursor.execute("""
#         UPDATE products
#         SET stock = stock - 1
#         WHERE product_id = %s
#     """, (1,))

#     cursor.execute("""
#         INSERT INTO orders (...)
#         VALUES (...)
#     """)

#     conn.commit()

# except Exception as e:
#     conn.rollback()
#     print("Transaction failed:", e)


# cursor.close()
# conn.close()




# best practice with seperate database.py and fetch in seperate file like products.py file 
from products import get_products

products = get_products()

for product in products:
    print(product)

