
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Output folder:", OUTPUT_DIR)


purchases = [
    1000, 1200, 1100, 1300, 1250,
    1150, 1050, 1400, 1180, 1350,
    1220, 1080, 1280, 1160, 1320,
    1020, 1240, 1380, 1120, 1260,
    1190, 1310, 1070, 1450, 50000
]

df = pd.DataFrame({
    "Customer": [
        f"Customer_{i}" for i in range(1, 26)
    ],
    "Purchase": purchases
})

# Save original dataset
df.to_csv(OUTPUT_DIR / "customers.csv", index=False)

print("\n--- Original Dataset ---")
print(df)


# ==========================================
# 3. DESCRIPTIVE STATISTICS
# ==========================================

mean_value = df["Purchase"].mean()
median_value = df["Purchase"].median()
std_value = df["Purchase"].std(ddof=0)
min_value = df["Purchase"].min()
max_value = df["Purchase"].max()

print("\n--- Descriptive Statistics ---")
print(df["Purchase"].describe())

print("Mean:", mean_value)
print("Median:", median_value)
print("Population Standard Deviation:", std_value)
print("Minimum:", min_value)
print("Maximum:", max_value)


# ==========================================
# 4. OUTLIER DETECTION USING IQR
# ==========================================

Q1 = df["Purchase"].quantile(0.25)
Q3 = df["Purchase"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df["IQR_Outlier"] = (
    (df["Purchase"] < lower_bound) |
    (df["Purchase"] > upper_bound)
)

print("\n--- IQR Method ---")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

iqr_outliers = df[df["IQR_Outlier"]]

print("\nPotential IQR Outliers:")
print(iqr_outliers[["Customer", "Purchase"]])


# ==========================================
# 5. OUTLIER DETECTION USING Z-SCORE
# ==========================================

df["Z_Score"] = (
    (df["Purchase"] - mean_value) / std_value
)

df["Z_Outlier"] = df["Z_Score"].abs() > 3

print("\n--- Z-Score Method ---")

print(
    df[
        ["Customer", "Purchase", "Z_Score", "Z_Outlier"]
    ].to_string(index=False)
)

z_outliers = df[df["Z_Outlier"]]

print("\nPotential Z-Score Outliers:")
print(z_outliers[["Customer", "Purchase", "Z_Score"]])


# ==========================================
# 6. COMPARE BOTH METHODS
# ==========================================

df["Potential_Outlier"] = (
    df["IQR_Outlier"] | df["Z_Outlier"]
)

print("\n--- IQR vs Z-Score Comparison ---")

print(
    df[
        [
            "Customer",
            "Purchase",
            "IQR_Outlier",
            "Z_Score",
            "Z_Outlier",
            "Potential_Outlier"
        ]
    ].to_string(index=False)
)

flagged = df[df["Potential_Outlier"]].copy()

print("\nObservations Flagged by Either Method:")
print(
    flagged[
        [
            "Customer",
            "Purchase",
            "IQR_Outlier",
            "Z_Score",
            "Z_Outlier"
        ]
    ]
)


# ==========================================
# 7. INVESTIGATE POTENTIAL OUTLIERS
# ==========================================

df["Investigation_Status"] = "Not flagged"

df.loc[
    df["Potential_Outlier"],
    "Investigation_Status"
] = "Needs verification"

print("\n--- Investigation Results ---")

print(
    df.loc[
        df["Potential_Outlier"],
        [
            "Customer",
            "Purchase",
            "Investigation_Status"
        ]
    ]
)

# An outlier is not automatically an error.
# Verify unusual transactions against original records.
# Do not delete genuine purchases just because they are large.


# ==========================================
# 8. CREATE ANALYSIS DATASET
# ==========================================

# No observations have been confirmed invalid.
# Therefore, keep all observations for now.

analysis_df = df.copy()

# If investigation later confirms an incorrect value,
# correct or exclude it based on verified evidence.
# Do not automatically remove all detected outliers.

print("\n--- Analysis Dataset ---")
print("Original observations:", len(df))
print("Analysis observations:", len(analysis_df))


# ==========================================
# 9. COMPARE STATISTICS BEFORE AND AFTER
# ==========================================

before_stats = df["Purchase"].agg(
    ["count", "mean", "median", "std", "min", "max"]
)

after_stats = analysis_df["Purchase"].agg(
    ["count", "mean", "median", "std", "min", "max"]
)

comparison = pd.DataFrame({
    "Before_Treatment": before_stats,
    "After_Treatment": after_stats
})

print("\n--- Before vs After Treatment ---")
print(comparison)

comparison.to_csv(
    OUTPUT_DIR / "statistics_comparison.csv"
)


# ==========================================
# 10. CREATE BOXPLOT
# ==========================================

plt.figure(figsize=(10, 5))

plt.boxplot(
    df["Purchase"],
    vert=False,
    showmeans=True
)

plt.title("Customer Purchase Amounts - Box Plot")
plt.xlabel("Purchase Amount")
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "box_plot.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("\nBox plot saved successfully.")


# ==========================================
# 11. SAVE OUTLIER RESULTS
# ==========================================

df.to_csv(
    OUTPUT_DIR / "outlier_results.csv",
    index=False
)

print("Outlier results saved successfully.")


# ==========================================
# 12. GENERATE MARKDOWN REPORT
# ==========================================

iqr_count = int(df["IQR_Outlier"].sum())
z_count = int(df["Z_Outlier"].sum())
combined_count = int(df["Potential_Outlier"].sum())

flagged_rows = df[df["Potential_Outlier"]]

if flagged_rows.empty:
    flagged_text = "No observations were flagged."
else:
    flagged_text = flagged_rows[
        ["Customer", "Purchase", "IQR_Outlier", "Z_Score", "Z_Outlier"]
    ].to_markdown(index=False)

report = f"""# Outlier Investigation Report

## 1. Objective

Investigate unusual customer purchase amounts using
descriptive statistics, the IQR method, Z-scores,
and a box plot.

## 2. Dataset

- Total observations: {len(df)}
- Numeric variable: Purchase
- Original dataset: customers.csv

## 3. Descriptive Statistics

- Mean: {mean_value:.2f}
- Median: {median_value:.2f}
- Population standard deviation: {std_value:.2f}
- Minimum purchase: {min_value:.2f}
- Maximum purchase: {max_value:.2f}

## 4. IQR Method

- Q1: {Q1:.2f}
- Q3: {Q3:.2f}
- IQR: {IQR:.2f}
- Lower bound: {lower_bound:.2f}
- Upper bound: {upper_bound:.2f}
- Number of flagged observations: {iqr_count}

An observation is flagged when it falls below the lower
bound or above the upper bound.

## 5. Z-Score Method

- Number of flagged observations: {z_count}
- Threshold: absolute Z-score greater than 3

A Z-score describes how many population standard
deviations an observation is from the mean.

## 6. Comparison of Methods

- IQR outliers: {iqr_count}
- Z-score outliers: {z_count}
- Flagged by either method: {combined_count}

### Flagged Observations

{flagged_text}

## 7. Investigation

Flagged observations require verification against original
transaction records, receipts, or purchase history.

A high purchase amount may be genuine. Statistical
detection alone does not establish that a transaction
is invalid.

## 8. Treatment Decision

No observations were automatically removed or changed.

The analysis dataset retains all {len(analysis_df)} observations
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
"""

(OUTPUT_DIR / "outlier_report.md").write_text(
    report,
    encoding="utf-8"
)

print("\nMarkdown report generated successfully.")


# ==========================================
# 13. FINAL OUTPUT SUMMARY
# ==========================================

print("\n--- PROJECT COMPLETED ---")
print("Output directory:", OUTPUT_DIR)

print("\nGenerated files:")

for file_path in sorted(OUTPUT_DIR.iterdir()):
    if file_path.is_file():
        print("-", file_path.name)
