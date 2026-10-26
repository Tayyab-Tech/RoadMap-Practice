# Image-Like Array

# Create a 6 × 6 array representing grayscale pixel values from 0–255.

# Requirements:

# Find pixels greater than 200.
# Replace pixels below 50 with 0.
# Increase every pixel by 20.
# Make sure values don't exceed 255.
# Calculate average brightness.
# Find the brightest pixel.

# Concepts: vectorization, boolean indexing, broadcasting, clipping.


import importlib
np = importlib.import_module("numpy")

arr = np.random.randint(0,256, size=(6,6))

print(arr)
print()
print(arr[arr>200])
print()
arr[arr<50] = 0
print(arr)
print()
arr = arr + 20
arr = np.clip(arr, 0, 255) # minimum element value = 0 and maximum element value = 255
print(arr)
print()
print(f"{arr.mean():.2f}")
print()
print(arr.max())