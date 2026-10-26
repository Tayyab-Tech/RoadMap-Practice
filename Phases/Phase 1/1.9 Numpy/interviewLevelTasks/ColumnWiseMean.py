# Task 6 — Column-wise Mean Centering

# Given:

# arr = np.array([
#     [10, 20, 30],
#     [20, 30, 40],
#     [30, 40, 50]
# ])

# Subtract the mean of each column from that column.

# The resulting array should have approximately:

# column mean = 0

# Concepts: axis, broadcasting.
import importlib
np = importlib.import_module("numpy")

arr = np.array([
    [10, 20, 30],
    [20, 30, 40],
    [30, 40, 50]
])

column_mean = arr.mean(axis=0)
print(column_mean)
centered = arr - column_mean

print(centered)
print(centered.mean(axis=0))