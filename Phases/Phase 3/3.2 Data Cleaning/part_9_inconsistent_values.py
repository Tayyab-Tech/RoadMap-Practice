# What are inconsistent values?
# Suppose you are analyzing customers from different cities:

# Raw value	Problem
# Lahore	Standard spelling
# lahore	Different capitalization
# Lahore	Extra spaces
# LAHORE	Uppercase
# Lahor	    Possible spelling mistake
# LHR	    Abbreviation that may mean Lahore

# These values might represent the same city, but a computer may count them as separate categories.

# For example, a report might incorrectly show six different city categories instead of one or two.

# Other common inconsistencies include:
# - Gender: Male, M, male, MALE
# - Status: Completed, complete, Done, COMPLETE
# - Boolean values: Yes, Y, True, 1
# - Units: kilograms versus pounds, or rupees versus dollars
# - Product names: iPhone 15, Iphone15, iPhone-15

# Important: Similar-looking values are not always equivalent. Decide the correct mapping using business rules or source documentation before replacing anything.

import pandas as pd

data = {
    "Customer": [
        "Ali", "Sara", "Ahmed", "Ayesha",
        "Usman", "Hina", "Bilal", "Noor"
    ],
    "City": [
        "Lahore", "lahore", " Lahore ",
        "LAHORE", "Lahor", "Karachi",
        "KARACHI ", "KHI"
    ],
    "Gender": [
        "Male", "M", "male", "F",
        "Female", "FEMALE", "Male", "female"
    ],
    "Status": [
        "Completed", "complete", "Done",
        "Pending", "PENDING", "In Progress",
        "in progress", "Complete"
    ]
}

df = pd.DataFrame(data)

# print(df)




# for column in ["City", "Gender", "Status"]:
#     print(f"\n{column}:")
#     print(df[column].value_counts(dropna=False))



# Standardize whitespace and capitalization

df["City"] = (
    df["City"]
    .str.strip()
    .str.title()
)

df["Gender"] = (
    df["Gender"]
    .str.strip()
    .str.lower()
)

df["Status"] = (
    df["Status"]
    .str.strip()
    .str.lower()
)

print(df[["City", "Gender", "Status"]])
print()

# Map known spelling variations

city_mapping = {
    "Lahor": "Lahore",
    "Lhr": "Lahore",
    "Khi": "Karachi"
}

df["City"] = df["City"].replace(city_mapping)

print(df["City"].value_counts())
print()

gender_mapping = {
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female"
}

df["Gender"] = (
    df["Gender"]
    .str.strip()
    .str.lower()
    .replace(gender_mapping)
)

print(df["Gender"].value_counts(dropna=False))
print()

status_mapping = {
    "completed": "Completed",
    "complete": "Completed",
    "done": "Completed",
    "pending": "Pending",
    "in progress": "In Progress"
}

df["Status"] = (
    df["Status"]
    .str.strip()
    .str.lower()
    .replace(status_mapping)
)
print(df["Status"].value_counts(dropna=False))
print()


print("Detect unexpected categories before replacing them \n")

allowed_statuses = [
    "Completed",
    "Pending",
    "In Progress",
    "Cancelled"
]

unexpected = df.loc[
    ~df["Status"].isin(allowed_statuses),
    "Status"
].dropna().unique()

print("Unexpected statuses:", unexpected)
print()

# You can also flag values without immediately changing them
df["Status_Needs_Review"] = ~df["Status"].isin(
    allowed_statuses
)

print(df[["Status", "Status_Needs_Review"]])
print()


