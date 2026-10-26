# KPI Business Insights

## Scope and caveat
These interpretations are generated from the accompanying **synthetic practice dataset**. They demonstrate how to translate KPIs into business questions; they are not claims about a real store.

## Results summary
The notebook calculates all KPIs from the CSV and prints exact values when run. Use the notebook output as the source of numeric results rather than manually copying figures into this document.

## How to interpret the KPIs

### Sales and order value
- **GMV** describes the pre-discount value of completed orders. Compare GMV with net sales to understand the effect of discounts and shipping assumptions.
- **Net sales revenue** includes shipping fees and excludes cancelled and returned orders under the project rules. This is a simplified recognition model; a real business should use its accounting definition of revenue.
- **AOV** is useful for tracking basket value over time and by marketing channel or category. A higher AOV does not automatically mean higher profitability, so review gross margin alongside it.

### Profitability
- **Estimated gross profit and margin** subtract estimated product costs from retained-order revenue. Categories with strong sales but weak margin may need supplier-cost, pricing, or discount review.
- **Estimated contribution after product and attributed marketing cost** is only a partial contribution measure. Do not treat it as net profit because operating, fulfillment, payment-processing, tax, and other costs are missing.
- Review discount levels together with margin. Discounts can increase order value or volume while reducing profit per order.

### Customer retention
- **Repeat-customer rate** describes repeat purchasing within this dataset's 90-day date window. It is not a long-term retention or cohort-retention measure.
- A low rate may indicate a short observation window, a naturally infrequent-purchase product mix, or a customer-experience issue. Check customer cohorts and purchase frequency before drawing conclusions.

### Operations
- **Cancellation rate** should be monitored by date, category, and channel. Investigate stock availability, delivery estimates, payment failures, and customer-initiated cancellations before deciding on corrective action.
- **Return rate** is a count-based rate, not a value-based rate. A small number of expensive returns can have a larger financial impact than the count rate suggests.

### Marketing
- **Marketing cost per retained order** and the **ROAS-like ratio** are directional only because marketing costs are illustrative order-level allocations. They are not substitutes for channel-level campaign reporting.
- Do not compare channels solely on attributed revenue. Include margin, cancellation/return rates, attribution windows, and full campaign spend.

## Recommended next steps
1. Replace the sample CSV with validated production data and document the source and refresh date.
2. Reconcile revenue and order counts with the store platform or finance system.
3. Add daily sessions by channel to calculate conversion rate (`orders ÷ sessions`).
4. Add complete campaign spend and a documented attribution model to calculate CAC and channel ROAS.
5. Add payment fees, shipping/fulfillment costs, taxes, and overhead to build a reliable profit measure.
6. Segment the KPIs by month, product category, and marketing channel, and compare against targets or prior periods.
7. Treat outliers and small sample sizes cautiously; investigate before removing any records.
