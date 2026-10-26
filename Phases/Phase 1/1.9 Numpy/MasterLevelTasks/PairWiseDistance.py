# Pairwise Distance

# Given three points:

# points = np.array([
#     [1, 2],
#     [4, 6],
#     [7, 3]
# ])

# Calculate the Euclidean distance between:

# Point 1 → Point 2
# Point 1 → Point 3
# Point 2 → Point 3

# Try to solve it using NumPy vector operations rather than loops.

import importlib
np = importlib.import_module("numpy")

points = np.array([
    [1, 2],
    [4, 6],
    [7, 3]
])

d1 = np.linalg.norm(points[0]-points[1])
d2 = np.linalg.norm(points[0]-points[2])
d3 = np.linalg.norm(points[1]-points[2])


print("P1 → P2:", d1)
print("P1 → P3:", d2)
print("P2 → P3:", d3)