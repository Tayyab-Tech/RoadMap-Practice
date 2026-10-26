# Find Second Largest

# Given:

# arr = np.array([10, 50, 20, 80, 40, 80, 60])

# Find:

# Largest value.
# Second-largest unique value.
# Index of the second-largest value.


import importlib
np = importlib.import_module("numpy")

arr = np.array([10, 50, 20, 80, 40, 80, 60])

unique = np.unique(arr)
print(unique)

largest = unique[-1]
sec_largest = unique[-2]

index = np.where(arr == sec_largest)[0][0]

print("Largest:", largest)
print("Second-largest:", sec_largest)
print("Index:", index)


# Then solve the same problem for a 2D array.


arr2 = np.array([
    [10, 50, 20],
    [80, 40, 80],
    [60, 30, 70]
])

unique = np.unique(arr2)

largest = unique[-1]
sec_largest = unique[-2]

index = np.argwhere(arr2 == sec_largest)[0]

print("Largest:", largest)
print("Second-largest:", sec_largest)
print("Index:", index)