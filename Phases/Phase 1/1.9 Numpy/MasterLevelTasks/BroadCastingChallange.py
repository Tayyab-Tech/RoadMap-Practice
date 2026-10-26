# Broadcasting Challenge

# Given:

# prices = np.array([
#     [100, 200, 300],
#     [150, 250, 350],
#     [120, 220, 320]
# ])

# Each column represents a product.

# Apply these discounts:

# Product 1 → 10%
# Product 2 → 20%
# Product 3 → 15%

# Use only broadcasting/vectorized operations.

# Then calculate the final prices.

import importlib
np = importlib.import_module("numpy")

prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [120, 220, 320]
])

discounts = np.array([0.10, 0.20, 0.15])
final_prices = prices * (1 - discounts)

print(final_prices)