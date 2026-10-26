
# Missing Values Cleaning Report

## Dataset overview
- Original rows: 5
- Rows after cleaning: 5
- Columns: 4

## Missing values before cleaning
Customer    0
Age         2
Salary      1
City        1

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
