# Task 4 — Central Limit Theorem Experiment

# Create a highly skewed population using:

# np.random.exponential()

# Generate at least 100,000 observations.

# Then perform the following experiment:

# Take 2,000 samples of size 5.
# Calculate the mean of every sample.
# Store those means.
# Repeat with sample sizes:
# 5
# 30
# 100
# For each sample size, calculate:
# Mean of sample means
# Standard deviation of sample means
# Compare the results with the population mean.

# Answer:

# As the sample size increases, what happens to the distribution of sample means and its spread?
# As the sample size increases, the distribution of sample means becomes more approximately normal and its spread decreases. The mean of the sample means stays close to the population mean.


import numpy as np

# -----------------------------------
# 1. Create highly skewed population
# -----------------------------------

np.random.seed(42)

population_size = 100_000

population = np.random.exponential(
    scale=10,
    size=population_size
)

# Population mean
population_mean = np.mean(population)

print("===== Population =====")
print(f"Population size: {len(population)}")
print(f"Population mean: {population_mean:.4f}")


# -----------------------------------
# 2. Function for sampling experiment
# -----------------------------------

def sampling_experiment(population, sample_size, number_of_samples=2000):

    sample_means = []

    for _ in range(number_of_samples):

        # Take random sample without replacement
        sample = np.random.choice(
            population,
            size=sample_size,
            replace=False
        )

        # Calculate sample mean
        sample_mean = np.mean(sample)

        # Store sample mean
        sample_means.append(sample_mean)

    return np.array(sample_means)


# -----------------------------------
# 3. Sample size = 5
# -----------------------------------

means_5 = sampling_experiment(
    population,
    sample_size=5
)

mean_5 = np.mean(means_5)
std_5 = np.std(means_5)


# -----------------------------------
# 4. Sample size = 30
# -----------------------------------

means_30 = sampling_experiment(
    population,
    sample_size=30
)

mean_30 = np.mean(means_30)
std_30 = np.std(means_30)


# -----------------------------------
# 5. Sample size = 100
# -----------------------------------

means_100 = sampling_experiment(
    population,
    sample_size=100
)

mean_100 = np.mean(means_100)
std_100 = np.std(means_100)


# -----------------------------------
# 6. Display results
# -----------------------------------

print("\n===== Central Limit Theorem Experiment =====")

print("\nSample Size: 5")
print(f"Mean of sample means: {mean_5:.4f}")
print(f"Standard deviation of sample means: {std_5:.4f}")

print("\nSample Size: 30")
print(f"Mean of sample means: {mean_30:.4f}")
print(f"Standard deviation of sample means: {std_30:.4f}")

print("\nSample Size: 100")
print(f"Mean of sample means: {mean_100:.4f}")
print(f"Standard deviation of sample means: {std_100:.4f}")


# -----------------------------------
# 7. Comparison with population mean
# -----------------------------------

print("\n===== Comparison with Population Mean =====")

print(f"Population mean: {population_mean:.4f}")
print(f"Sample size 5:   {mean_5:.4f}")
print(f"Sample size 30:  {mean_30:.4f}")
print(f"Sample size 100: {mean_100:.4f}")