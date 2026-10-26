# Complete Array Analysis

# Create a random 5 × 5 integer array between 1 and 100.

# Find:

# Shape
# Dimensions
# Number of elements
# Data type
# Maximum
# Minimum
# Mean
# Standard deviation
# Position of maximum
# Position of minimum

import importlib
np = importlib.import_module("numpy")

arr = np.random.randint(1, 101, size=(5, 5))
print(arr)
print()
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.max())
print(arr.min())
print(arr.mean())
print(f"{arr.std():.2f}")
max_row,max_column = np.unravel_index(np.argmax(arr),arr.shape)
print(f"Maximum number row index : {max_row} \n Maximum number column index : {max_column}")
min_row,min_column = np.unravel_index(np.argmin(arr),arr.shape)
print(f"Minimum number row index : {min_row} \n Minimum number column index : {min_column}")