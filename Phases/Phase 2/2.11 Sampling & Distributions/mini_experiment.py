import numpy as np
import pandas as pd

np.random.seed(42)

# 1. Create population
population = np.random.exponential(
    scale=500,
    size=100000
)
print(len(population), "population values created.")
population_mean = np.mean(population)

print("Population mean:", population_mean)


# 2. Repeated sampling
sample_means = []

for _ in range(5000):

    sample = np.random.choice(
        population,
        size=50,
        replace=False
    )

    sample_mean = np.mean(sample)

    sample_means.append(sample_mean)


# 3. Convert to Pandas Series
sample_means = pd.Series(sample_means)


# 4. Analyze sampling distribution
print("\nSampling Distribution")
print("----------------------")

print("Mean:",
      sample_means.mean())

print("Median:",
      sample_means.median())

print("Standard deviation:",
      sample_means.std())

print("Minimum:",
      sample_means.min())

print("Maximum:",
      sample_means.max())