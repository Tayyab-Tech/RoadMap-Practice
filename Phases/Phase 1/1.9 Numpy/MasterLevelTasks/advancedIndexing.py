# Advanced Indexing

# Given:

# arr = np.arange(1, 26).reshape(5, 5)

# Extract:

# First row
# Last row
# First column
# Last column
# Main diagonal
# Anti-diagonal
# Center element
# Four corner elements
# Middle 3 × 3
# Every second row and column

# No loops.

import importlib
np = importlib.import_module("numpy")

arr = np.arange(1, 26).reshape(5, 5)
print(arr)
print()
print(arr[0])
print(arr[-1])
print(arr[:,0])
print(arr[:,-1])
print(np.diag(arr))
print(np.diag(np.fliplr(arr)))
print(arr[2,2])
print(arr[[0,0,-1,-1],[0,-1,0,-1]])
print(arr[1:4,1:4])
print(arr[::2,::2])