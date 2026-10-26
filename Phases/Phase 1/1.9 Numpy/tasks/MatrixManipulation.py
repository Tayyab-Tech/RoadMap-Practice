# Create a 4 × 4 NumPy array containing numbers from 1 to 16.

# Requirements:

# Print the first row.
# Print the last row.
# Print the second column.
# Extract the middle 2 × 2 matrix.
# Replace all values greater than 10 with 0.
# Calculate the sum of every row.
# Calculate the sum of every column.

# Concepts: 2D arrays, indexing, slicing, boolean indexing, axis.


import importlib

np = importlib.import_module("numpy")

numbers = np.arange(1,17).reshape(4,4)

print(numbers[0])
print(numbers[-1])
print(numbers[:,1])
print(numbers[1:3,1:3])
numbers[numbers > 10] = 0
print(numbers)
print(numbers.sum(axis=1))
print(numbers.sum(axis=0))