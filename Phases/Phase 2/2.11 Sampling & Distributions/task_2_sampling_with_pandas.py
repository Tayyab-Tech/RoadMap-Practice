# Create a Pandas DataFrame containing 5,000 customers with:

# customer_id
# age
# monthly_spending

# Generate:

# age: 18–70
# monthly_spending: normally distributed around 50,000 with standard deviation 10,000

# Then:

# Take a random sample of 200 customers using df.sample().
# Calculate the average spending of the population.
# Calculate the average spending of the sample.
# Calculate the difference between them.
# Repeat the sampling 100 times and store every sample mean.
# Calculate the mean of those 100 sample means.



import numpy as np
import pandas as pd

# Reproducible results
np.random.seed(42)

# -----------------------------------
# 1. Create population of 5,000 customers
# -----------------------------------

df = pd.DataFrame({
    "customer_id": np.arange(1, 5001),
    "age": np.random.randint(18, 71, size=5000),
    "monthly_spending": np.random.normal(
        loc=50000,
        scale=10000,
        size=5000
    )
})

# -----------------------------------
# 2. Take a random sample of 200
# -----------------------------------

sample = df.sample(n=200, random_state=42)

# -----------------------------------
# 3. Population average spending
# -----------------------------------

population_mean = df["monthly_spending"].mean()

# -----------------------------------
# 4. Sample average spending
# -----------------------------------

sample_mean = sample["monthly_spending"].mean()

# -----------------------------------
# 5. Difference between population
#    mean and sample mean
# -----------------------------------

difference = abs(population_mean - sample_mean)

# -----------------------------------
# 6. Repeat sampling 100 times
# -----------------------------------

sample_means = []

for i in range(100):
    sample = df.sample(n=200)
    mean = sample["monthly_spending"].mean()
    sample_means.append(mean)

# -----------------------------------
# 7. Mean of the 100 sample means
# -----------------------------------

mean_of_sample_means = np.mean(sample_means)


# -----------------------------------
# Display results
# -----------------------------------

print("===== Population Information =====")
print(f"Number of customers: {len(df)}")
print(f"Population mean spending: {population_mean:.2f}")

print("\n===== One Random Sample =====")
print(f"Sample size: {len(sample)}")
print(f"Sample mean spending: {sample_mean:.2f}")
print(f"Difference: {difference:.2f}")

print("\n===== 100 Repeated Samples =====")
print(f"Number of samples: {len(sample_means)}")
print(f"Mean of 100 sample means: {mean_of_sample_means:.2f}")