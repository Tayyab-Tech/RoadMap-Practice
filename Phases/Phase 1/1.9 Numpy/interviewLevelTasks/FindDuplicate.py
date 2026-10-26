# Given:

# arr = np.array([10, 20, 30, 20, 40, 10, 50, 30])

# Find all duplicate values without manually checking each element with a loop.
import importlib
np = importlib.import_module("numpy")

arr = np.array([10, 20, 30, 20, 40, 10, 50, 30])
value, counts = np.unique(arr,return_counts=True)
print(value)
print(counts)
duplicate = value[counts>1]
print(duplicate)