
import pandas as pd
import numpy as np
from pathlib import Path

# 1. Create the sample dataset
data = {
    "Customer": ["Ali", "Sara", "Ahmed", "Zain", "Ayesha"],
    "Age": [22, np.nan, 28, 25, np.nan],
    "Salary": [50000, 60000, np.nan, 45000, 55000],
    "City": ["Lahore", "Karachi", "Lahore", np.nan, "Islamabad"]
}

df = pd.DataFrame(data)

# 2. Save the original dataset
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "raw_customers.csv", index=False)

# 3. Record the original state
rows_before = len(df)
missing_before = df.isna().sum()

print("Missing values before cleaning:")
print(missing_before)

print("\nMissing percentages:")
print((df.isna().mean() * 100).round(2))

# 4. Work on a copy
clean_df = df.copy()

# 5. Fill numerical columns with their medians
for column in ["Age", "Salary"]:
    clean_df[column] = clean_df[column].fillna(
        clean_df[column].median()
    )

# 6. Preserve unknown city information
clean_df["City"] = clean_df["City"].fillna("Unknown")

# 7. Validate
missing_after = clean_df.isna().sum()

print("\nMissing values after cleaning:")
print(missing_after)

print("\nCleaned dataset:")
print(clean_df)

assert len(clean_df) == rows_before
assert clean_df["Age"].notna().all()
assert clean_df["Salary"].notna().all()
assert clean_df["City"].notna().all()

# 8. Export the cleaned dataset
clean_df.to_csv(
    output_dir / "clean_customers.csv",
    index=False
)

# 9. Create a documented report
report = f"""
# Missing Values Cleaning Report

## Dataset overview
- Original rows: {rows_before}
- Rows after cleaning: {len(clean_df)}
- Columns: {len(clean_df.columns)}

## Missing values before cleaning
{missing_before.to_string()}

## Treatment decisions
- Age: Missing values filled with the observed median.
- Salary: Missing values filled with the observed median.
- City: Missing values labelled as Unknown.
- Rows were preserved.

## Validation
- Age has no remaining missing values.
- Salary has no remaining missing values.
- City has no remaining missing values.
- Row count was preserved.

## Limitations
Median imputation is a demonstration, not proof
that these replacements represent the true values.
The treatment should be reviewed against the data
source and the intended analysis.

## Output
data/clean_customers.csv
"""

Path("data/cleaning_missing_report.md").write_text(
    report,
    encoding="utf-8"
)

print("\nCleaning completed.")
print("Saved: data/clean_customers.csv")
print("Saved: data/cleaning_missing_report.md")
