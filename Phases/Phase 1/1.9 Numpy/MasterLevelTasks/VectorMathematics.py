# Vector Mathematics

# Given:

# a = np.array([3, 4, 5])
# b = np.array([2, 1, 3])

# Calculate:

# a + b
# a - b
# a * b
# a / b
# Dot product
# Magnitude of a
# Magnitude of b
# Unit vector of a
# Cross product

# Then determine whether the vectors are perpendicular.

import importlib
np = importlib.import_module("numpy")

a = np.array([3, 4, 5])
b = np.array([2, 1, 3])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(np.dot(a,b))
print(np.linalg.norm(a))
print(np.linalg.norm(b))
print(a/np.linalg.norm(a))
print(np.cross(a,b))
print(np.isclose(np.dot(a,b),0))