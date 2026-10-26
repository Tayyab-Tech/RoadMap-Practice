# Broadcasting + Statistics

# Given:

# data = np.array([
#     [10, 20, 30],
#     [20, 40, 60],
#     [30, 60, 90],
#     [40, 80, 120]
# ])

# Perform:

# Column-wise mean.
# Column-wise standard deviation.
# Standardize every column using:
# z = (x - mean) / std
# Verify that each resulting column has approximately mean 0 and standard deviation 1.

# This is a very important ML-style NumPy operation.


import importlib
np = importlib.import_module("numpy")

data = np.array([
    [10, 20, 30],
    [20, 40, 60],
    [30, 60, 90],
    [40, 80, 120]
])
mean = data.mean(axis=0)
print(mean)
std = data.std(axis=0)
print(std)
z = (data-mean)/std
print(z)

print(np.round(z.mean(axis=0),2))
print(z.std(axis=0))