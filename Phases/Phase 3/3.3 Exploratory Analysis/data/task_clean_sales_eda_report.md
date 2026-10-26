# EDA Insight & Business Analysis — Clean Sales Dataset

**Source file:** `E:\RoadMap Practice\Phase 3\3.3 Exploratory Analysis\data\clean_sales.csv`  
**Rows:** 20 | **Columns:** 7  
**Source policy:** This report was generated only after `data/clean_sales.csv` was found; no fallback sample was used.

### 1. Quantity distribution
- **Finding:** Quantity is right-skewed based on sample skewness 1.156.
- **Evidence:** n=20, mean=4.00, median=2.50, min=1.00, max=12.00, Q1=1.75, Q3=5.50, IQR=3.75, Tukey-fence candidates=1
- **Interpretation:** The middle 50% spans 1.75 to 5.50 units; the mean-versus-median difference and skewness describe asymmetry. 1 values fall beyond the 1.5×IQR fences and merit checking.
- **Limitation:** Tukey fences flag unusual observations, not proven errors. Small samples and mixed product types can distort distribution shape.

### 2. Weight_kg distribution
- **Finding:** Weight_kg is right-skewed based on sample skewness 0.917.
- **Evidence:** n=20, mean=3.28, median=2.30, min=0.40, max=9.00, Q1=1.10, Q3=4.62, IQR=3.52, Tukey-fence candidates=0
- **Interpretation:** The middle 50% spans 1.10 to 4.62 kg; the mean-versus-median difference and skewness describe asymmetry. 0 values fall beyond the 1.5×IQR fences and merit checking.
- **Limitation:** Tukey fences flag unusual observations, not proven errors. Small samples and mixed product types can distort distribution shape.

### 3. Category segment
- **Finding:** Grocery leads by Total_Quantity.
- **Evidence:** Leading category by Total_Quantity: Grocery = 46; rows=5; unique orders=5; mean quantity per row=9.20
- **Interpretation:** Total quantity measures units, row count measures records, unique orders deduplicates Order_ID, and average quantity describes typical quantity per row; the leaders can differ.
- **Limitation:** These descriptive totals do not adjust for time period, missing group labels, customer base, revenue, costs, or profit.

### 4. City segment
- **Finding:** Lahore leads by Total_Quantity.
- **Evidence:** Leading city by Total_Quantity: Lahore = 35; rows=6; unique orders=6; mean quantity per row=5.83
- **Interpretation:** Total quantity measures units, row count measures records, unique orders deduplicates Order_ID, and average quantity describes typical quantity per row; the leaders can differ.
- **Limitation:** These descriptive totals do not adjust for time period, missing group labels, customer base, revenue, costs, or profit.

### 5. Order status
- **Finding:** Completed is the most frequent status.
- **Evidence:** Completed: 10 rows (50.0% of all rows).
- **Interpretation:** This is the most common recorded status in the available rows.
- **Limitation:** Status row counts are not necessarily unique orders and may include multiple product rows per order; pending/returned/cancelled meanings should be verified.

### 6. Quantity–weight relationship
- **Finding:** Pearson correlation is 0.114, a weak positive linear association in the paired records.
- **Evidence:** Paired n=20; Pearson r=0.114.
- **Interpretation:** Review the scatter plot for clustering, non-linearity, and influential points. If weight is per item, a positive association may be expected; if it is total order weight, interpretation differs.
- **Limitation:** Correlation is observational and does not prove causation. With a small paired sample, r can be unstable and sensitive to individual points.

### 7. Needs_Review investigation
- **Finding:** 2 record(s) are flagged for manual review.
- **Evidence:** Flagged records: 2 of 20 (10.0%); exported to `task_clean_sales_needs_review.csv`.
- **Interpretation:** Check each flagged row against the original order/product source, especially quantity, weight, category, city, status, and any documented review reason. A flag means investigate, not automatically an error.
- **Limitation:** Without the source transaction or a documented flag rule, this analysis cannot determine whether any flagged row is incorrect.

### 8. Source and data quality
- **Finding:** Analysis uses the intended cleaned input file and does not silently fall back to generated sample data.
- **Evidence:** Loaded `E:\RoadMap Practice\Phase 3\3.3 Exploratory Analysis\data\clean_sales.csv`; shape=20 rows × 7 columns; exact duplicate rows=0; missing cells=0.
- **Interpretation:** All statistics and segment comparisons in this run derive from the file printed at load time.
- **Limitation:** The notebook cannot independently prove the file's upstream provenance; ensure this file is the actual Phase 3.2 cleaned export.

## Business recommendations

### Recommendation 1
- **Action:** Resolve the Needs_Review queue before making operational decisions.
- **Evidence:** 2 record(s) flagged when Needs_Review is available; see task_clean_sales_needs_review.csv.
- **Expected benefit:** Reduce the risk of basing reports on unverified quantity, weight, status, or location values.
- **Validate first:** Compare each flagged row with the source order/product record and document whether the flag is a true error, valid exception, or false positive.

### Recommendation 2
- **Action:** Use Grocery as a candidate for a focused stock and replenishment review, not an automatic stock increase.
- **Evidence:** It has the highest category total quantity (46 units) in this dataset.
- **Expected benefit:** Align inventory review with observed unit volume and reduce avoidable stockouts or overstocking if the pattern persists.
- **Validate first:** Check a longer date range, stockouts, lead times, seasonality, returns, unique orders, and product-level demand before changing reorder points.

### Recommendation 3
- **Action:** Review fulfillment capacity and delivery performance for Lahore, the leading city by total quantity.
- **Evidence:** Lahore has the highest city total quantity (35 units).
- **Expected benefit:** Identify whether fulfillment capacity should be adjusted to match observed workload.
- **Validate first:** Compare unique orders, time period, delivery cost, service levels, customer base, and geographic coverage; total quantity alone does not justify resource reallocation.

## Important limitations

- Quantity and order-row counts are not revenue or profitability. Profit decisions require prices, discounts, product costs, shipping/fulfillment costs, and return costs.
- Row counts, unique order counts, total quantity, and average quantity are different measures.
- Potential outliers and Needs_Review flags require source verification; neither alone proves an error.
- Small samples, missing fields, and unknown time coverage limit generalization.
