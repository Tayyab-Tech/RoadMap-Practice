# Given:

# arr = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])

# Normalize each row independently so that every row has a maximum value of 1.

# You must use broadcasting.

import importlib
np = importlib.import_module("numpy")


arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

normalize = arr / arr.max(axis=1, keepdims=True)

print(normalize)