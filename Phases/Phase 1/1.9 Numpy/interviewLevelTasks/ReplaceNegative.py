# Given:

# arr = np.array([-10, 20, -5, 30, -15, 40])

# Replace every negative number with 0.

# Expected:

# [0, 20, 0, 30, 0, 40]

# Restriction: Don't use a loop.

import importlib
np = importlib.import_module("numpy")

arr = np.array([-10, 20, -5, 30, -15, 40])

arr[arr<0]=0

print(arr)