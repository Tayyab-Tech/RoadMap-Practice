# Given:
# arr = np.array([10, 20, 30, 40, 50])
# Normalize the array using:
# (x - min) / (max - min)
# Expected range:
# 0 → 1
# Concepts: vectorization, aggregation, broadcasting.
import importlib
np = importlib.import_module("numpy")

arr = np.array([10, 20, 30, 40, 50])
normalize = (arr - arr.min()) / (arr.max() - arr.min())
print(normalize)