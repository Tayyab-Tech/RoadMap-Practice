# A company's employee salaries are approximately normally distributed:

# Mean = 80,000
# Standard deviation = 15,000

# Using NumPy:

# Generate 10,000 salaries using np.random.normal().
# Calculate the actual mean and standard deviation.
# Calculate z-scores for every salary.
# Find employees whose z-score is greater than 2.
# Find employees whose z-score is less than -2.
# Calculate what percentage of employees fall within:
# ±1 standard deviation
# ±2 standard deviations
# ±3 standard deviations

# Compare your results with the 68–95–99.7 rule.





import numpy as np

# -----------------------------------
# Given information
# -----------------------------------

mean = 80000
std = 15000
number_of_employees = 10000

# Reproducible results
np.random.seed(42)


# -----------------------------------
# 1. Generate 10,000 salaries
# -----------------------------------

salaries = np.random.normal(
    loc=mean,
    scale=std,
    size=number_of_employees
)


# -----------------------------------
# 2. Calculate actual mean and
#    standard deviation
# -----------------------------------

actual_mean = np.mean(salaries)
actual_std = np.std(salaries)


# -----------------------------------
# 3. Calculate z-scores
# -----------------------------------

z_scores = (salaries - mean) / std


# -----------------------------------
# 4. Employees with z-score > 2
# -----------------------------------

above_2 = z_scores > 2
employees_above_2 = salaries[above_2]

count_above_2 = len(employees_above_2)


# -----------------------------------
# 5. Employees with z-score < -2
# -----------------------------------

below_minus_2 = z_scores < -2
employees_below_minus_2 = salaries[below_minus_2]

count_below_minus_2 = len(employees_below_minus_2)


# -----------------------------------
# 6. Percentage within ±1, ±2, ±3
#    standard deviations
# -----------------------------------

within_1 = np.abs(z_scores) <= 1
within_2 = np.abs(z_scores) <= 2
within_3 = np.abs(z_scores) <= 3

percentage_1 = np.mean(within_1) * 100
percentage_2 = np.mean(within_2) * 100
percentage_3 = np.mean(within_3) * 100


# -----------------------------------
# Display results
# -----------------------------------

print("===== Normal Distribution + Z-Scores =====")

print("\n--- Given Values ---")
print(f"Mean: ${mean:,.2f}")
print(f"Standard Deviation: ${std:,.2f}")
print(f"Number of Employees: {number_of_employees}")

print("\n--- Actual Distribution ---")
print(f"Actual Mean: ${actual_mean:,.2f}")
print(f"Actual Standard Deviation: ${actual_std:,.2f}")

print("\n--- Z-Score Results ---")
print(f"Employees with z-score > 2: {count_above_2}")
print(f"Employees with z-score < -2: {count_below_minus_2}")

print("\n--- Percentage Within Standard Deviations ---")
print(f"Within ±1 SD: {percentage_1:.2f}%")
print(f"Within ±2 SD: {percentage_2:.2f}%")
print(f"Within ±3 SD: {percentage_3:.2f}%")

print("\n--- 68–95–99.7 Rule Comparison ---")
print(f"±1 SD: Actual {percentage_1:.2f}% | Expected ~68%")
print(f"±2 SD: Actual {percentage_2:.2f}% | Expected ~95%")
print(f"±3 SD: Actual {percentage_3:.2f}% | Expected ~99.7%")