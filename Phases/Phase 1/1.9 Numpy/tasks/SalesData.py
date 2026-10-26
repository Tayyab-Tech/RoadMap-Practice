# Create a NumPy array representing sales of 4 products over 3 months:

# Product 1 → 120, 150, 180
# Product 2 → 200, 170, 220
# Product 3 → 90, 110, 130
# Product 4 → 250, 230, 280

# Requirements:

# Find total sales of each product.
# Find total sales for each month.
# Find the product with the highest total sales.
# Find the month with the highest total sales.
# Calculate the average sales of each product.

# Concepts: 2D arrays, axis, aggregation, indexing.
import importlib
np = importlib.import_module("numpy")

sales = np.array([
    [120, 150, 180],
    [200, 170, 220],
    [90, 110, 130],
    [250, 230, 280]
])

product_total = sales.sum(axis=1)
month_total = sales.sum(axis=0)
print("Product totals:", product_total)
print("Month totals:", month_total)
print("Highest product:", np.argmax(product_total) + 1)
print("Highest month:", np.argmax(month_total) + 1)
print("Product averages:", sales.mean(axis=1))