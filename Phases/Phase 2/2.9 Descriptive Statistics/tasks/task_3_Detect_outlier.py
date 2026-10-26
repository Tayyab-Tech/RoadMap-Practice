import numpy as np
data = np.array([20, 22, 24, 25, 26, 27, 28, 30, 32, 35, 100])


# Using NumPy:

# Calculate mean and median.
# Calculate Q1 and Q3.
# Calculate IQR.
# Calculate lower and upper bounds using the 1.5 × IQR rule.
# Find the potential outlier(s).
# Explain how the outlier affects the mean and standard deviation.

mean = np.mean(data)
median = np.median(data)

Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)

IQR = Q3 - Q1

lower_boundary = Q1 - 1.5*IQR
upper_boundary = Q3 + 1.5*IQR

outlier = data[(data<lower_boundary)|(data>upper_boundary)]

std = np.std(data)


print("Mean:", mean)
print("Median:", median)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower bound:", lower_boundary)
print("Upper bound:", upper_boundary)
print("Outliers:", outlier)
print("Standard deviation:", std)