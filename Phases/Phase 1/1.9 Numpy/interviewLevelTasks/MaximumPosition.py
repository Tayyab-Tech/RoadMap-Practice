# Find the Maximum Position
# Given:

# arr = np.array([
#     [12, 45, 23],
#     [67, 34, 89],
#     [21, 90, 56]
# ])

# Find:

# Maximum value
# Its row index
# Its column index

# Hint: Explore argmax() and unravel_index().

import importlib
np = importlib.import_module("numpy")

arr = np.array([
    [12, 45, 23],
    [67, 34, 89],
    [21, 90, 56]
])

max_position = np.argmax(arr)
# print(max_position)
row, column = np.unravel_index(max_position,arr.shape)
print("Maximum value:", arr[row, column])
print("Row index:", row)
print("Column index:", column)