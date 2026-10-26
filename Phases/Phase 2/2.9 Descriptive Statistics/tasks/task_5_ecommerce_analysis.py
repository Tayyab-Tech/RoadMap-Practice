import pandas as pd
import numpy as np


df = pd.DataFrame({
    "order_id": range(1, 21),

    "customer_age": [
        22, 25, 28, 31, 35,
        24, 27, 30, 33, 29,
        41, 45, 38, 26, 32,
        36, 23, 40, 34, 50
    ],

    "order_amount": [
        120, 250, 180, 2500, 450,
        275, 390, 210, 500, 350,
        1500, 425, 700, 290, 550,
        480, 160, 800, 230, 5000
    ]
})

# Using Pandas + NumPy:

# Calculate mean, median, variance and standard deviation of order_amount.
# Calculate P25, P50, P75 and P90.
# Calculate Q1, Q3 and IQR.
# Detect potential outliers using the 1.5 × IQR rule.
# Calculate the same statistics for customer_age.
# Compare mean vs median for order_amount.
# Explain how the outliers affect the mean and standard deviation.
# Write a 5–7 line analyst conclusion explaining the dataset's center, spread, and outliers.

# =========================================================
# 1. Order Amount Statistics
# =========================================================

amount = df["order_amount"]

mean_amount = amount.mean()
median_amount = amount.median()
variance_amount = amount.var()
std_amount = amount.std()

print("\n=== Order Amount Statistics ===")
print("Mean:", mean_amount)
print("Median:", median_amount)
print("Variance:", variance_amount)
print("Standard Deviation:", std_amount)


# =========================================================
# 2. P25, P50, P75 and P90
# =========================================================

p25_amount = np.percentile(amount, 25)
p50_amount = np.percentile(amount, 50)
p75_amount = np.percentile(amount, 75)
p90_amount = np.percentile(amount, 90)

print("\n=== Order Amount Percentiles ===")
print("P25:", p25_amount)
print("P50:", p50_amount)
print("P75:", p75_amount)
print("P90:", p90_amount)


# =========================================================
# 3. Q1, Q3 and IQR
# =========================================================

q1_amount = amount.quantile(0.25)
q3_amount = amount.quantile(0.75)

iqr_amount = q3_amount - q1_amount

print("\n=== Order Amount IQR ===")
print("Q1:", q1_amount)
print("Q3:", q3_amount)
print("IQR:", iqr_amount)


# =========================================================
# 4. Detect Order Amount Outliers
# =========================================================

lower_amount = q1_amount - 1.5 * iqr_amount
upper_amount = q3_amount + 1.5 * iqr_amount

amount_outliers = df[
    (df["order_amount"] < lower_amount) |
    (df["order_amount"] > upper_amount)
]

print("\n=== Order Amount Outliers ===")
print("Lower Bound:", lower_amount)
print("Upper Bound:", upper_amount)
print(amount_outliers)


# =========================================================
# 5. Customer Age Statistics
# =========================================================

age = df["customer_age"]

mean_age = age.mean()
median_age = age.median()
variance_age = age.var()
std_age = age.std()

p25_age = np.percentile(age, 25)
p50_age = np.percentile(age, 50)
p75_age = np.percentile(age, 75)
p90_age = np.percentile(age, 90)

q1_age = age.quantile(0.25)
q3_age = age.quantile(0.75)
iqr_age = q3_age - q1_age

lower_age = q1_age - 1.5 * iqr_age
upper_age = q3_age + 1.5 * iqr_age

age_outliers = df[
    (df["customer_age"] < lower_age) |
    (df["customer_age"] > upper_age)
]

print("\n=== Customer Age Statistics ===")
print("Mean:", mean_age)
print("Median:", median_age)
print("Variance:", variance_age)
print("Standard Deviation:", std_age)

print("\nPercentiles:")
print("P25:", p25_age)
print("P50:", p50_age)
print("P75:", p75_age)
print("P90:", p90_age)

print("\nQ1:", q1_age)
print("Q3:", q3_age)
print("IQR:", iqr_age)

print("\nAge Lower Bound:", lower_age)
print("Age Upper Bound:", upper_age)
print("Age Outliers:")
print(age_outliers)


# =========================================================
# 6. Mean vs Median
# =========================================================

print("\n=== Mean vs Median ===")
print("Order Amount Mean:", mean_amount)
print("Order Amount Median:", median_amount)


# =========================================================
# 7. Outlier Effect
# =========================================================

print("\n=== Outlier Effect ===")
print("The large order amount increases the mean and standard deviation because it is far from the other orders.")