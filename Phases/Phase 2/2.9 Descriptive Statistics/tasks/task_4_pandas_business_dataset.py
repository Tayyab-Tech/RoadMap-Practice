import pandas as pd

df = pd.DataFrame({
    "employee": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha",
                 "Hamza", "Zara", "Bilal", "Hina", "Omar"],
    "salary": [40000, 45000, 48000, 50000, 52000,
               55000, 58000, 60000, 65000, 200000]
})

# Using Pandas:

# Use describe().
# Calculate mean salary.
# Calculate median salary.
# Calculate variance and standard deviation.
# Calculate Q1, Q3 and IQR.
# Detect potential salary outliers.
# Explain whether mean or median better represents the typical salary and why.

print("=== Describe ===")
print(df["salary"].describe())


mean_salary = df["salary"].mean()
median_salary = df["salary"].median()

variance = df["salary"].var()
std = df["salary"].std()

q1 = df["salary"].quantile(0.25)
q3 = df["salary"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5*iqr
upper_bound = q3 + 1.5*iqr


outlier = df[(df["salary"]<lower_bound)|(df["salary"]>upper_bound)]



print("\nMean:", mean_salary)
print("Median:", median_salary)
print("Variance:", variance)
print("Standard Deviation:", std)

print("\nQ1:", q1)
print("Q3:", q3)
print("IQR:", iqr)

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nPotential Outliers:")
print(outlier)