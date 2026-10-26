import numpy as np
data = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40]

# Using NumPy, calculate:

# Mean
# Median
# Population variance
# Population standard deviation
# Minimum
# Maximum


mean = np.mean(data)
median = np.median(data)

population_variance = np.var(data)
population_standard_deviation = np.std(data)

minimum = np.min(data)
maximum = np.max(data)

print("Mean:", mean)
print("Median:", median)
print("Population Variance:", population_variance)
print("Population Standard Deviation:", population_standard_deviation)
print("Minimum:", minimum)
print("Maximum:", maximum)

