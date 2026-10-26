# Create a NumPy array containing temperatures in Celsius:

# [0, 10, 20, 25, 30, 35, 40]

# Convert all values to Fahrenheit using NumPy vectorization.

# Formula:

# F = C × 9/5 + 32

# Requirements:

# Do not use a for loop.
# Print both Celsius and Fahrenheit arrays.
# Find temperatures where Fahrenheit is greater than 90.

# Concepts: vector operations, broadcasting, boolean indexing.

import importlib
np = importlib.import_module("numpy")

celcius = np.array([0, 10, 20, 25, 30, 35, 40])

fahrenheit = celcius * (9/5) + 32

print(celcius)
print(fahrenheit)
print(fahrenheit[fahrenheit>90])