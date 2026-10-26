# Duplicate Records Cleaning Report

## Dataset overview
- Original rows: 7
- Final rows: 5
- Rows removed: 2

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
- Exact duplicates remaining: 0
- Row counts reconcile: True

## Limitations
- Business-key conflicts require separate investigation.
- Exact matching does not detect all duplicate customers.
- The sample assumes identical transaction rows are
  accidental duplicates.

## Output
data/clean_orders.csv
