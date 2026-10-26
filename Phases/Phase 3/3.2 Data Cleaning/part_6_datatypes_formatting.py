import pandas as pd
import numpy as np

data = {
    "Customer": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Age": ["25", "30", "unknown", "22"],
    "Salary": ["50000", "60,000", "45000", "70,000"],
    "JoinDate": [
        "2026-01-15",
        "15/02/2026",
        "2026/04/03",
        "2026-04-20"
    ],
    "City": [" Lahore ", "lahore", "Karachi", "LAHORE"]
}

df = pd.DataFrame(data)

print(df)
print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()


print("\n Converting to numbers : \n")

df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

print(df["Age"])
print(df["Age"].dtype)


# df["Salary"] = pd.to_numeric(
#     df["Salary"],
#     errors="coerce"
# )

# print(df["Salary"].mean())



# if salary contains commas or currency symbols, we need to clean the data before converting it to numeric
df["Salary"] = (
    df["Salary"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.replace("Rs.", "", regex=False)
    .str.strip()
)

df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

print(df["Salary"])
print(df["Salary"].dtype)



# to convert date column

df["JoinDate"] = pd.to_datetime(
    df["JoinDate"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

print(df["JoinDate"])
print(df["JoinDate"].dtype)

df["JoinYear"] = df["JoinDate"].dt.year
df["JoinMonth"] = df["JoinDate"].dt.month

print(df[["JoinDate", "JoinYear", "JoinMonth"]])





print("\n Standardize text formatting : \n")


df["Customer"] = (
    df["Customer"]
    .astype("string")
    .str.strip()
    .str.title()
)

print(df["Customer"])


df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.title()
)

print(df["City"])


# df["Email"] = df["Email"].astype("string").str.strip().str.lower()