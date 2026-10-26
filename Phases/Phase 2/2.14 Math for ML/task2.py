import numpy as np

# Feature matrix: 3 students, 2 features
X = np.array([
    [2, 3],
    [4, 5],
    [6, 7]
])

weights = np.array([3, 2])
bias = 1

# 1. Print shape
print("Shape of X:", X.shape)

# 2. Calculate predictions
predictions = X @ weights + bias
print("Predictions:", predictions)

# 3. Sum of all elements
total = np.sum(X)
print("Sum of X:", total)

# 4. Create another matrix of the same shape
another_matrix = np.ones(X.shape, dtype=int) * 10

addition = X + another_matrix

print("Another matrix:")
print(another_matrix)

print("Element-wise addition:")
print(addition)

# Optional: display the matrix multiplication separately
print("Matrix multiplication X @ weights:", X @ weights)