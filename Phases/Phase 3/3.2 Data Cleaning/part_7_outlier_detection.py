


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Customer": [
        "Ali", "Sara", "Ahmed", "Ayesha",
        "Usman", "Hina", "Zain", "Bilal",
        "Noor", "Hamza"
    ],
    "Purchase": [
        1000, 1200, 1100, 1300, 1250,
        1150, 1050, 1400, 1180, 5000
    ]
}

df = pd.DataFrame(data)

print(df)
print()
print(df["Purchase"].describe())




print("\nDetecting outliers using IQR method:\n")


print("\n Method 1 — IQR (Interquartile Range) : \n")


Q1 = df["Purchase"].quantile(0.25)
Q3 = df["Purchase"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

outliers = df[(df["Purchase"] < lower_bound) | (df["Purchase"] > upper_bound)]

print("\nPotential outliers:")
print(outliers)



print("\n Method 2 — Z-score : \n")


mean_value = df["Purchase"].mean()
std_value = df["Purchase"].std(ddof=0)

df["Z_Score"] = (
    (df["Purchase"] - mean_value) / std_value
)

df["Potential_Outlier"] = (
    df["Z_Score"].abs() > 3 # or use 2 instead of 3 if there is a need to be more strict in detecting outliers
)

print(
    df[["Customer", "Purchase", "Z_Score",
        "Potential_Outlier"]]
)




# Visualize outliers with a box plot

# plt.figure(figsize=(8, 4))

# plt.boxplot(df["Purchase"], vert=False)

# plt.title("Purchase Amounts — Outlier Detection")
# plt.xlabel("Purchase Amount")

# plt.show()


print("\n Method 3 — Using a copy of the dataset to flag potential outliers : \n")

# Preserve the raw dataset
raw_df = df.copy()

# Recalculate IQR boundaries from Purchase
Q1 = raw_df["Purchase"].quantile(0.25)
Q3 = raw_df["Purchase"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Flag potential outliers
raw_df["Is_Outlier"] = (
    (raw_df["Purchase"] < lower) |
    (raw_df["Purchase"] > upper)
)

# Filter for a specific analysis, if justified
analysis_df = raw_df.loc[
    ~raw_df["Is_Outlier"]
].copy()

print("Original rows:", len(raw_df))
print("Flagged rows:", raw_df["Is_Outlier"].sum())
print("Rows in filtered analysis:", len(analysis_df))




print("\nComparing mean and median before and after filtering out potential outliers:\n")

original_mean = df["Purchase"].mean()
original_median = df["Purchase"].median()

print("\nBefore filtering :")
print("Mean:", original_mean)
print("Median:", original_median)

print("\nAfter filtering :")
print("Mean:", analysis_df["Purchase"].mean())
print("Median:", analysis_df["Purchase"].median())