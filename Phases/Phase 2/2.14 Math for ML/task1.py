import numpy as np

# Create two vectors
features = np.array([2, 5, 8])
weights = np.array([3, 4, 2])

# 1. Vector addition
addition = features + weights

# 2. Vector subtraction
subtraction = features - weights

# 3. Multiply features by 3
multiplication = features * 3

# 4. Dot product
dot_product = np.dot(features, weights)

# 5. Mean of features
mean_features = np.mean(features)

# Print results
print("Features:", features)
print("Weights:", weights)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Features multiplied by 3:", multiplication)
print("Dot product:", dot_product)
print("Mean of features:", mean_features)
