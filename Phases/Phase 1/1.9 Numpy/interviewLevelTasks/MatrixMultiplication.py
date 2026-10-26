# Matrix Multiplication

# Create:

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])

# B = np.array([
#     [5, 6],
#     [7, 8]
# ])

# Calculate:

# Element-wise multiplication.
# Matrix multiplication.
# Transpose of A.
# Determinant of A.
# Inverse of A.

# Important: Understand why A * B and A @ B produce different results.

import importlib
np = importlib.import_module("numpy")

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a*b) # element multiplication
print(a@b) # matrix multiplication
print(a.T) # a transpose
print(np.linalg.det(a)) # a determinant
print(np.linalg.inv(a)) # a inverse