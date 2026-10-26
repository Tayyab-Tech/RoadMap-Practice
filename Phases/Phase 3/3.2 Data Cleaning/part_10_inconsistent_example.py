
import pandas as pd
from pathlib import Path

# ==========================================
# 1. PROJECT PATHS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)

INPUT_FILE = DATA_DIR / "messy_sales.csv"
OUTPUT_FILE = DATA_DIR / "clean_sales.csv"
REPORT_FILE = DATA_DIR / "cleaning_inconsistent_values_report.md"

print("Data folder:", DATA_DIR)


# ==========================================
# 2. CREATE MESSY SALES DATASET
# ==========================================

# Create sample data only if the input file
# does not already exist. Existing data is preserved.

if not INPUT_FILE.exists():

    data = {
        "Order_ID": list(range(1001, 1021)),

        "City": [
            "lahore", "Lahore ", " LAHORE", "LHR",
            "karachi", "Karachi ", "KARACHI", "KHI",
            "islamabad", "Islamabad ", "ISB", "isb",
            "lahore", "Karachi", "unknown city", " Peshawar ",
            "PESHAWAR", "Faisalabad", "faisalabad ", "Multan"
        ],

        "Category": [
            "electronics", "Electronics ", "ELECTRONICS",
            "Electronic", "clothing", "Clothing ",
            "CLOTHING", "apparel", "grocery", "Grocery ",
            "GROCERY", "food", "electronics", "clothing",
            "unknown category", "Furniture", "furniture ",
            "Grocery", "electronics", "Home & Kitchen"
        ],

        "Order_Status": [
            "completed", "Completed ", "COMPLETED",
            "delivered", "pending", " Pending ",
            "PENDING", "in progress", "cancelled",
            "Cancelled ", "CANCELLED", "canceled",
            "shipped", "processing", "unknown status",
            "Returned", "returned ", "Completed",
            "Pending", "shipped "
        ],

        "Quantity": [
            2, 1, 3, 1, 4,
            2, 1, 3, 5, 2,
            1, 4, 2, 3, 1,
            2, 1, 5, 2, 3
        ],

        "Weight": [
            "500 g", "1 kg", "250 g", "2 kg",
            "750 g", "1.5 kg", "1000 g", "3 kg",
            "500 g", "2.5 kg", "750 g", "1 kg",
            "1500 g", "2 kg", "300 g", "1 kg",
            "2000 g", "0.5 kg", "750 g", "1 kg"
        ]
    }

    messy_df = pd.DataFrame(data)
    messy_df.to_csv(INPUT_FILE, index=False)

    print("\nCreated sample messy_sales.csv")


# ==========================================
# 3. LOAD DATASET
# ==========================================

df = pd.read_csv(INPUT_FILE)

original_row_count = len(df)

print("\n--- Original Dataset ---")
print(df.to_string(index=False))


# ==========================================
# 4. INSPECT DISTINCT VALUES BEFORE CLEANING
# ==========================================

print("\n--- DISTINCT VALUES BEFORE CLEANING ---")

for column in ["City", "Category", "Order_Status", "Weight"]:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False).to_string())


# ==========================================
# 5. STANDARDIZE WHITESPACE AND CAPITALIZATION
# ==========================================

# Apply to text columns only.
# Preserve missing values as missing values.

text_columns = ["City", "Category", "Order_Status"]

for column in text_columns:
    df[column] = df[column].map(
        lambda value: (
            value.strip().casefold()
            if isinstance(value, str)
            else value
        )
    )


# ==========================================
# 6. EXPLICIT MAPPING DICTIONARIES
# ==========================================

# Only confirmed variations should be mapped.
# Unknown values remain unchanged for manual review.

city_mapping = {
    "lahore": "Lahore",
    "lhr": "Lahore",

    "karachi": "Karachi",
    "khi": "Karachi",

    "islamabad": "Islamabad",
    "isb": "Islamabad",

    "peshawar": "Peshawar",
    "faisalabad": "Faisalabad",
    "multan": "Multan"
}

category_mapping = {
    "electronics": "Electronics",
    "electronic": "Electronics",

    "clothing": "Clothing",
    "apparel": "Clothing",

    "grocery": "Grocery",
    "food": "Grocery",

    "furniture": "Furniture",
    "home & kitchen": "Home & Kitchen"
}

status_mapping = {
    "completed": "Completed",
    "delivered": "Delivered",

    "pending": "Pending",

    "in progress": "In Progress",
    "processing": "Processing",

    "cancelled": "Cancelled",
    "canceled": "Cancelled",

    "shipped": "Shipped",
    "returned": "Returned"
}


# ==========================================
# 7. APPLY APPROVED MAPPINGS
# ==========================================

df["City"] = df["City"].map(city_mapping).fillna(
    df["City"]
)

df["Category"] = df["Category"].map(
    category_mapping
).fillna(df["Category"])

df["Order_Status"] = df["Order_Status"].map(
    status_mapping
).fillna(df["Order_Status"])


# ==========================================
# 8. CONVERT MIXED WEIGHT UNITS TO KG
# ==========================================

def convert_weight_to_kg(value):
    """
    Convert supported g/kg strings to kilograms.
    Return None for unsupported or missing values.
    """
    if pd.isna(value):
        return None

    text = str(value).strip().casefold()

    try:
        if text.endswith("kg"):
            number = float(text[:-2].strip())
            return number

        elif text.endswith("g"):
            number = float(text[:-1].strip())
            return number / 1000

        else:
            return None

    except ValueError:
        return None


df["Weight_kg"] = df["Weight"].apply(convert_weight_to_kg)


# Flag missing or unrecognized weight values.
df["Weight_Review"] = df["Weight_kg"].isna()


# ==========================================
# 9. FLAG UNKNOWN VALUES FOR MANUAL REVIEW
# ==========================================

approved_cities = {
    "Lahore",
    "Karachi",
    "Islamabad",
    "Peshawar",
    "Faisalabad",
    "Multan"
}

approved_categories = {
    "Electronics",
    "Clothing",
    "Grocery",
    "Furniture",
    "Home & Kitchen"
}

approved_statuses = {
    "Completed",
    "Delivered",
    "Pending",
    "In Progress",
    "Processing",
    "Cancelled",
    "Shipped",
    "Returned"
}


df["City_Review"] = (
    ~df["City"].isin(approved_cities)
)

df["Category_Review"] = (
    ~df["Category"].isin(approved_categories)
)

df["Status_Review"] = (
    ~df["Order_Status"].isin(approved_statuses)
)


df["Needs_Review"] = (
    df["City_Review"]
    | df["Category_Review"]
    | df["Status_Review"]
    | df["Weight_Review"]
)


# ==========================================
# 10. VALIDATE STANDARDIZED VALUES
# ==========================================

valid_city_rows = df["City"].isin(approved_cities)
valid_category_rows = df["Category"].isin(approved_categories)
valid_status_rows = df["Order_Status"].isin(approved_statuses)

print("\n--- VALIDATION RESULTS ---")

print(
    "Valid city rows:",
    int(valid_city_rows.sum()),
    "/",
    len(df)
)

print(
    "Valid category rows:",
    int(valid_category_rows.sum()),
    "/",
    len(df)
)

print(
    "Valid order status rows:",
    int(valid_status_rows.sum()),
    "/",
    len(df)
)

print(
    "Rows needing manual review:",
    int(df["Needs_Review"].sum())
)

# Show unresolved distinct values.
print("\n--- UNKNOWN CITY VALUES ---")
print(sorted(df.loc[df["City_Review"], "City"].dropna().unique().tolist()))

print("\n--- UNKNOWN CATEGORY VALUES ---")
print(sorted(df.loc[df["Category_Review"], "Category"].dropna().unique().tolist()))

print("\n--- UNKNOWN STATUS VALUES ---")
print(sorted(df.loc[df["Status_Review"], "Order_Status"].dropna().unique().tolist()))


# ==========================================
# 11. SAVE CLEANED DATASET
# ==========================================

df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved:", OUTPUT_FILE)


# ==========================================
# 12. GENERATE CLEANING REPORT
# ==========================================

city_review_count = int(df["City_Review"].sum())
category_review_count = int(df["Category_Review"].sum())
status_review_count = int(df["Status_Review"].sum())
weight_review_count = int(df["Weight_Review"].sum())
rows_needing_review = int(df["Needs_Review"].sum())

unknown_cities = sorted(
    df.loc[df["City_Review"], "City"].dropna().unique().tolist()
)

unknown_categories = sorted(
    df.loc[df["Category_Review"], "Category"].dropna().unique().tolist()
)

unknown_statuses = sorted(
    df.loc[df["Status_Review"], "Order_Status"].dropna().unique().tolist()
)

report = f"""# Sales Dataset Cleaning Report

## 1. Objective

Standardize inconsistent city names, product categories,
order statuses, and weight units.

## 2. Row Counts

- Original rows: {original_row_count}
- Final rows: {len(df)}
- Rows added: 0
- Rows deleted: {original_row_count - len(df)}
- Rows requiring manual review: {rows_needing_review}

No rows were deleted during cleaning.

## 3. Cleaning Rules

### Whitespace and capitalization

- Removed leading and trailing whitespace.
- Converted text to a consistent case before mapping.
- Standardized approved values to their canonical labels.

### City mapping

- LHR -> Lahore
- KHI -> Karachi
- ISB -> Islamabad
- Confirmed spelling and capitalization variations were standardized.
- Unknown cities were not guessed or automatically assigned.

### Category mapping

- Electronic -> Electronics
- Apparel -> Clothing
- Food -> Grocery
- Confirmed variations were mapped to approved categories.
- Unknown categories remain flagged for review.

### Order status mapping

- Canceled -> Cancelled
- Confirmed capitalization and whitespace variations were standardized.
- Different statuses such as Delivered and Completed remain separate.
- Unknown statuses remain flagged for review.

### Weight conversion

- Grams were converted to kilograms by dividing by 1000.
- Kilogram values were retained in kilograms.
- Unsupported or missing weight values are flagged for review.
- Original Weight column was retained for traceability.

## 4. Validation

Approved city values: {sorted(approved_cities)}

Approved category values: {sorted(approved_categories)}

Approved order statuses: {sorted(approved_statuses)}

Rows with valid cities: {int(valid_city_rows.sum())}/{len(df)}

Rows with valid categories: {int(valid_category_rows.sum())}/{len(df)}

Rows with valid order statuses: {int(valid_status_rows.sum())}/{len(df)}

## 5. Unresolved Issues

### Unknown cities

{unknown_cities if unknown_cities else "None"}

Rows flagged for city review: {city_review_count}

### Unknown categories

{unknown_categories if unknown_categories else "None"}

Rows flagged for category review: {category_review_count}

### Unknown order statuses

{unknown_statuses if unknown_statuses else "None"}

Rows flagged for status review: {status_review_count}

Rows flagged for weight review: {weight_review_count}

Unknown values require confirmation before they can be
mapped to approved categories.

## 6. Output

- Input: messy_sales.csv
- Cleaned dataset: clean_sales.csv
- Standardized fields: City, Category, Order_Status
- Converted field: Weight_kg
- Review flags: City_Review, Category_Review,
  Status_Review, Weight_Review, Needs_Review

## 7. Conclusion

Known variations were standardized using explicit mappings.
Mixed weight units were converted to kilograms.
Unknown values were retained and flagged for manual review
instead of being silently assigned an assumed category.
"""

REPORT_FILE.write_text(report, encoding="utf-8")

print("\nCleaning report saved:", REPORT_FILE)


# ==========================================
# 13. FINAL SUMMARY
# ==========================================

print("\n--- FINAL CLEANED DATA ---")

print(
    df[
        [
            "Order_ID",
            "City",
            "Category",
            "Order_Status",
            "Weight",
            "Weight_kg",
            "Needs_Review"
        ]
    ].to_string(index=False)
)

print("\n--- PROJECT COMPLETED ---")
print("Files saved in:", DATA_DIR)

for file_path in sorted(DATA_DIR.iterdir()):
    if file_path.is_file():
        print("-", file_path.name)
