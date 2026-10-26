
import pandas as pd
from pathlib import Path

# 1. Create sample raw data
data = {
    "OrderID": [101, 102, 103, 102, 104, 105, 105],
    "Customer": [
        "Ali", "Sara", "Ahmed", "Sara",
        "Zain", "Ayesha", "Ayesha"
    ],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Mouse",
        "Monitor", "Phone", "Phone"
    ],
    "Amount": [
        100000, 2000, 4000, 2000,
        25000, 80000, 80000
    ]
}

df = pd.DataFrame(data)

# 2. Preserve the raw data
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "raw_orders.csv", index=False)

rows_before = len(df)

# 3. Detect exact duplicates
duplicate_mask = df.duplicated(keep=False)
duplicate_groups = df[duplicate_mask]

print("Rows before cleaning:", rows_before)
print("Later duplicate occurrences:", df.duplicated().sum())
print("All rows in duplicate groups:")
print(duplicate_groups)

# 4. Remove exact duplicates
clean_df = df.drop_duplicates().copy()

rows_after = len(clean_df)
rows_removed = rows_before - rows_after

# 5. Validate the result
assert not clean_df.duplicated().any()
assert rows_after + rows_removed == rows_before

print("\nRows after cleaning:", rows_after)
print("Rows removed:", rows_removed)
print("Duplicates remaining:", clean_df.duplicated().sum())

# 6. Export the clean dataset
clean_df.to_csv(
    output_dir / "clean_orders.csv",
    index=False
)

# 7. Document the cleaning process
report = f"""
# Duplicate Records Cleaning Report

## Dataset overview
- Original rows: {rows_before}
- Final rows: {rows_after}
- Rows removed: {rows_removed}

## Detection
- Method: Exact row comparison
- Pandas method: duplicated()
- Retention rule: Keep first occurrence

## Treatment
- Exact duplicate rows were removed.
- The raw dataset was preserved.
- No records were removed solely because
  their OrderID appeared more than once.

## Validation
- Exact duplicates remaining: {clean_df.duplicated().sum()}
- Row counts reconcile: {rows_after + rows_removed == rows_before}

## Limitations
- Business-key conflicts require separate investigation.
- Exact matching does not detect all duplicate customers.
- The sample assumes identical transaction rows are
  accidental duplicates.

## Output
data/clean_orders.csv
"""

Path("data/cleaning_duplicate_report.md").write_text(
    report.strip() + "\n",
    encoding="utf-8"
)

print("\nSaved data/clean_orders.csv")
print("Saved data/cleaning_duplicate_report.md")
