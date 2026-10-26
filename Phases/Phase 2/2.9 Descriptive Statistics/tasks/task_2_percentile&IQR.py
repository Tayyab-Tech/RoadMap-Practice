import numpy as np
data = np.array([10, 15, 20, 22, 25, 28, 30, 35, 40, 45, 50, 60])

# Using NumPy:

# Calculate P25, P50, P75 and P90.
# Identify Q1 and Q3.
# Calculate IQR.
# Calculate the lower and upper outlier boundaries.
# Explain what the IQR tells you about the dataset.

p25 = np.percentile(data,25)
p50 = np.percentile(data,50)
p75 = np.percentile(data,75)
p90 = np.percentile(data,90)


q1 = np.percentile(data,25)
q3 = np.percentile(data,75)

iqr = q3-q1

lower_boundry = q1 - 1.5*iqr
upper_boundry = q3 + 1.5*iqr


outliers = data[(data < lower_boundry) | (data > upper_boundry)]



print("P25:", p25)
print("P50:", p50)
print("P75:", p75)
print("P90:", p90)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower boundary:", lower_boundry)
print("Upper boundary:", upper_boundry)
print("Outliers:", outliers)