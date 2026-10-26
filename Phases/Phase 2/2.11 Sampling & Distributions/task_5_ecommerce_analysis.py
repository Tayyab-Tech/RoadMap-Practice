# Create a Pandas DataFrame representing 50,000 customers:

# customer_id
# age
# orders
# total_spending

# Generate realistic random data using NumPy. Make total_spending right-skewed using an exponential or lognormal distribution.

# Perform a complete statistical investigation:

# Calculate population:
# Mean
# Median
# Standard deviation
# 25th percentile
# 75th percentile
# Take a random sample of 500 customers.
# Compare population and sample statistics.
# Repeat sampling 1,000 times and calculate the sample mean of total_spending each time.
# Store the 1,000 means in a Pandas Series/DataFrame.
# Calculate:
# Mean of sample means
# Standard deviation of sample means
# Minimum sample mean
# Maximum sample mean

# Repeat the experiment with sample sizes:

# 10
# 50
# 100
# 500
# Determine how increasing sample size affects the variability of the sample mean.
# Explain in your own words:

# Why can the original total_spending distribution be highly skewed while the distribution of its sample means becomes approximately normal?



import numpy as np
import pandas as pd


# ============================================================
# 1. CREATE POPULATION
# ============================================================

np.random.seed(42)

N = 50_000

customer_id = np.arange(1, N + 1)

# Realistic customer ages: 18 to 70
age = np.random.randint(18, 71, size=N)

# Number of orders: 1 to 15
orders = np.random.randint(1, 16, size=N)

# Right-skewed spending using lognormal distribution
total_spending = np.random.lognormal(
    mean=7,
    sigma=1,
    size=N
)

# Create DataFrame
df = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "orders": orders,
    "total_spending": total_spending
})


print("Population DataFrame:")
print(df.head())

print("\nPopulation shape:")
print(df.shape)


# ============================================================
# 2. POPULATION STATISTICS
# ============================================================

population_mean = df["total_spending"].mean()
population_median = df["total_spending"].median()
population_std = df["total_spending"].std(ddof=0)
population_q25 = df["total_spending"].quantile(0.25)
population_q75 = df["total_spending"].quantile(0.75)


print("\n========== POPULATION STATISTICS ==========")

print("Mean:", population_mean)
print("Median:", population_median)
print("Standard Deviation:", population_std)
print("25th Percentile:", population_q25)
print("75th Percentile:", population_q75)


# ============================================================
# 3. TAKE ONE RANDOM SAMPLE OF 500 CUSTOMERS
# ============================================================

sample_500 = df.sample(
    n=500,
    random_state=42
)


print("\n========== SAMPLE OF 500 ==========")
print(sample_500.head())


# ============================================================
# 4. COMPARE POPULATION AND SAMPLE STATISTICS
# ============================================================

sample_mean = sample_500["total_spending"].mean()
sample_median = sample_500["total_spending"].median()
sample_std = sample_500["total_spending"].std(ddof=1)
sample_q25 = sample_500["total_spending"].quantile(0.25)
sample_q75 = sample_500["total_spending"].quantile(0.75)


comparison = pd.DataFrame({
    "Statistic": [
        "Mean",
        "Median",
        "Standard Deviation",
        "25th Percentile",
        "75th Percentile"
    ],
    "Population": [
        population_mean,
        population_median,
        population_std,
        population_q25,
        population_q75
    ],
    "Sample (500)": [
        sample_mean,
        sample_median,
        sample_std,
        sample_q25,
        sample_q75
    ]
})


print("\n========== POPULATION VS SAMPLE ==========")
print(comparison)


# ============================================================
# 5. TAKE 1,000 SAMPLES OF SIZE 500
# ============================================================

sample_means_500 = []

for i in range(1000):

    sample = df.sample(n=500)

    mean = sample["total_spending"].mean()

    sample_means_500.append(mean)


# Convert to Pandas Series
sample_means_500 = pd.Series(
    sample_means_500,
    name="sample_mean"
)


print("\n========== 1,000 SAMPLE MEANS ==========")
print(sample_means_500.head())


# ============================================================
# 6. STATISTICS OF SAMPLE MEANS
# ============================================================

mean_of_means = sample_means_500.mean()
std_of_means = sample_means_500.std(ddof=1)
minimum_mean = sample_means_500.min()
maximum_mean = sample_means_500.max()


print("\n========== SAMPLE MEANS STATISTICS ==========")

print("Mean of sample means:", mean_of_means)
print("Standard deviation of sample means:", std_of_means)
print("Minimum sample mean:", minimum_mean)
print("Maximum sample mean:", maximum_mean)


# ============================================================
# 7. REPEAT EXPERIMENT FOR DIFFERENT SAMPLE SIZES
# ============================================================

sample_sizes = [10, 50, 100, 500]

results = []

for size in sample_sizes:

    means = []

    for i in range(1000):

        sample = df.sample(n=size)

        sample_mean = sample["total_spending"].mean()

        means.append(sample_mean)

    means = np.array(means)

    results.append({
        "sample_size": size,
        "mean_of_means": np.mean(means),
        "std_of_sample_means": np.std(means, ddof=1),
        "minimum": np.min(means),
        "maximum": np.max(means)
    })


# Convert results into DataFrame
results_df = pd.DataFrame(results)


print("\n========== SAMPLING EXPERIMENT ==========")
print(results_df)


# ============================================================
# 8. COMPARE VARIABILITY
# ============================================================

print("\n========== VARIABILITY BY SAMPLE SIZE ==========")

print(
    results_df[
        ["sample_size", "std_of_sample_means"]
    ]
)


# ============================================================
# 9. FINAL INTERPRETATION
# ============================================================

print("\n========== CONCLUSION ==========")

print("""
As sample size increases, the standard deviation of the sample means decreases.

Small samples such as 10 have more variability.

Larger samples such as 500 have much less variability.

The original total_spending distribution is highly right-skewed because some customers spend much more than others.

However, when we repeatedly take random samples and calculate their means, the distribution of those means becomes approximately normal.

This happens because of the Central Limit Theorem.

The Central Limit Theorem says that when we take many random samples from a population and calculate their means, the distribution of those sample means approaches a normal distribution as the sample size becomes sufficiently large.

Therefore:

Population distribution -> highly skewed

Individual samples -> can still be skewed

Distribution of many sample means -> approximately normal

Larger sample size -> less variability in sample means
""")