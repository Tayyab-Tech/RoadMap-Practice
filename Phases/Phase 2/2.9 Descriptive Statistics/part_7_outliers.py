
import numpy as np
data = np.array([
    12, 15, 18, 20, 22,
    24, 25, 27, 30, 32,
    35, 36, 38, 40, 200
])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)


outliers = data[
    (data < lower_bound) |
    (data > upper_bound)
]


print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("Outliers:", outliers)