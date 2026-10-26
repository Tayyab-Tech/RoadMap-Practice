# Task 7 — Vector Similarity
# Given two vectors:
# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])

# Calculate:

# 1.  Dot product 
# 2.  Magnitude of each vector 
# 3.  Cosine similarity 

# Cosine similarity:
# (a · b) / (||a||x||b||)

import importlib
np = importlib.import_module("numpy")

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

dot_product = np.dot(a, b)
print(dot_product)

mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)

print(mag_a)
print(mag_b)


cosine_similarity = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosine_similarity)