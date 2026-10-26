# Outlier Investigation Report

## 1. Objective

Investigate unusual customer purchase amounts using
descriptive statistics, the IQR method, Z-scores,
and a box plot.

## 2. Dataset

- Total observations: 25
- Numeric variable: Purchase
- Original dataset: customers.csv

## 3. Descriptive Statistics

- Mean: 3163.20
- Median: 1220.00
- Population standard deviation: 9561.26
- Minimum purchase: 1000.00
- Maximum purchase: 50000.00

## 4. IQR Method

- Q1: 1120.00
- Q3: 1310.00
- IQR: 190.00
- Lower bound: 835.00
- Upper bound: 1595.00
- Number of flagged observations: 1

An observation is flagged when it falls below the lower
bound or above the upper bound.

## 5. Z-Score Method

- Number of flagged observations: 1
- Threshold: absolute Z-score greater than 3

A Z-score describes how many population standard
deviations an observation is from the mean.

## 6. Comparison of Methods

- IQR outliers: 1
- Z-score outliers: 1
- Flagged by either method: 1

### Flagged Observations

| Customer    |   Purchase | IQR_Outlier   |   Z_Score | Z_Outlier   |
|:------------|-----------:|:--------------|----------:|:------------|
| Customer_25 |      50000 | True          |    4.8986 | True        |

## 7. Investigation

Flagged observations require verification against original
transaction records, receipts, or purchase history.

A high purchase amount may be genuine. Statistical
detection alone does not establish that a transaction
is invalid.

## 8. Treatment Decision

No observations were automatically removed or changed.

The analysis dataset retains all 25 observations
because no transaction has been confirmed invalid.

If evidence confirms a data-entry error, correct or
exclude the affected observation and document the reason.

## 9. Before-and-After Comparison

See statistics_comparison.csv.

Because no observations were changed, statistics before
and after treatment should be identical.

## 10. Box Plot Interpretation

See box_plot.png.

Points beyond the whiskers are potential outliers.
They should be investigated before any treatment decision.

## 11. Conclusion

IQR and Z-score methods identify unusual observations
using different statistical rules.

The final decision to retain, correct, or exclude a
transaction must be based on evidence and the purpose
of the analysis, not just an outlier flag.
