# Sales Dataset Cleaning Report

## 1. Objective

Standardize inconsistent city names, product categories,
order statuses, and weight units.

## 2. Row Counts

- Original rows: 20
- Final rows: 20
- Rows added: 0
- Rows deleted: 0
- Rows requiring manual review: 1

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

Approved city values: ['Faisalabad', 'Islamabad', 'Karachi', 'Lahore', 'Multan', 'Peshawar']

Approved category values: ['Clothing', 'Electronics', 'Furniture', 'Grocery', 'Home & Kitchen']

Approved order statuses: ['Cancelled', 'Completed', 'Delivered', 'In Progress', 'Pending', 'Processing', 'Returned', 'Shipped']

Rows with valid cities: 19/20

Rows with valid categories: 19/20

Rows with valid order statuses: 19/20

## 5. Unresolved Issues

### Unknown cities

['unknown city']

Rows flagged for city review: 1

### Unknown categories

['unknown category']

Rows flagged for category review: 1

### Unknown order statuses

['unknown status']

Rows flagged for status review: 1

Rows flagged for weight review: 0

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
