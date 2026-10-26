# Random Sampling with NumPy

# Create a population containing 10,000 student marks between 0 and 100.

# Requirements:

# Generate the population using NumPy.
# Take a random sample of 100 students without replacement.
# Calculate:
# Population mean
# Sample mean
# Population standard deviation
# Sample standard deviation
# Compare the population and sample statistics.
# Use np.random.seed(42) so your result is reproducible.



import numpy as np

# Reproducible results
np.random.seed(42)

# 1. Create population of 10,000 student marks
population = np.random.randint(0, 101, size=10000)

# 2. Take a random sample of 100 students without replacement
sample = np.random.choice(population, size=100, replace=False)

# 3. Calculate statistics

# Population statistics
population_mean = np.mean(population)
population_std = np.std(population)

# Sample statistics
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)


# Display results
print("===== Random Sampling with NumPy =====")

print(f"Population size: {len(population)}")
print(f"Sample size: {len(sample)}")

print("\n--- Population Statistics ---")
print(f"Population Mean: {population_mean:.2f}")
print(f"Population Standard Deviation: {population_std:.2f}")

print("\n--- Sample Statistics ---")
print(f"Sample Mean: {sample_mean:.2f}")
print(f"Sample Standard Deviation: {sample_std:.2f}")

print("\n--- Comparison ---")
print(f"Mean Difference: {abs(population_mean - sample_mean):.2f}")
print(f"Standard Deviation Difference: {abs(population_std - sample_std):.2f}")