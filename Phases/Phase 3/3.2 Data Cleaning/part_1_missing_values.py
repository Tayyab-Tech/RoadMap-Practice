import pandas as pd
import numpy as np

data = {
    "Customer": ["Ali", "Sara", "Ahmed", "Zain", "Ayesha"],
    "Age": [22, np.nan, 28, 25, np.nan],
    "Salary": [50000, 60000, np.nan, 45000, 55000],
    "City": ["Lahore", "Karachi", "Lahore", np.nan, "Islamabad"]
}

df = pd.DataFrame(data)

print(df)

print("\nMissing Values in Each Column:\n")
print(df.isnull().sum())



print("\nCalculate the percentage of missing values : \n")
missing_count = df.isnull().sum()
missing_percent = (df.isnull().mean() * 100).round(2)

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percent": missing_percent
})

print(missing_report)



print("\n Display rows with missing values : \n")
print(df[df.isnull().any(axis=1)])



print("\n inspect missing ages : \n")
print(df[df['Age'].isna()])




# ========================= Four main ways to handle missing values ================

print("\n Method 1: Remove missing rows : \n")

# clean_df = df.dropna()
# print(clean_df)

# also remove using special column 
# clean_df = df.dropna(subset=["Age"])
# print(clean_df)



print("\n Method 2: Fill numerical values with the mean : \n")

# df_mean = df.copy()

# mean_age = df_mean["Age"].mean()
# df_mean["Age"] = df_mean["Age"].fillna(mean_age)

# print("Mean age:", mean_age)
# print(df_mean)


print("\n Method 3: Fill numerical values with the median : \n")

# df_median = df.copy()

# median_age = df_median["Age"].median()
# df_median["Age"] = df_median["Age"].fillna(median_age)

# print("Median age:", median_age)

# df_median["Salary"] = df_median["Salary"].fillna(
#     df_median["Salary"].median()
# )
# print(df_median)




print("\n Method 4: Fill categorical values : \n")

# Option A — Fill with the mode

# df_mode = df.copy()

# mode_city = df_mode["City"].mode()[0]
# df_mode["City"] = df_mode["City"].fillna(mode_city)

# print(df_mode)


# Option B — Use an explicit unknown category

df_unknown = df.copy()

df_unknown["City"] = df_unknown["City"].fillna("Unknown")

print(df_unknown)



print("Missing values after cleaning:")
print(df.isna().sum())

print("\nRemaining missing-value percentage:")
print((df.isna().mean() * 100).round(2))

print("\nDataset shape:")
print(df.shape)

print("\nData types:")
print(df.dtypes)