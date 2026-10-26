# E-commerce KPI Dictionary

## Purpose
This dictionary defines the KPIs used in the project, how they are calculated, the assumptions behind them, and the data needed to calculate them.

## Dataset grain and conventions
- **Grain:** one row per order.
- `unit_price` and `unit_cost` are per-unit amounts; `quantity` is the number of units ordered.
- `discount_pct` is a fraction (for example, `0.10` means 10%).
- An order is considered **completed** when `order_status == "Completed"`.
- Revenue and profit metrics use completed orders only. Returned completed orders are excluded from net sales and profit in this simplified model.
- `marketing_cost` is an illustrative order-attributed cost, not necessarily the full campaign spend.
- The dataset is synthetic and intended for practice, not business reporting.

## KPI definitions

| KPI | Formula | Population / Filters | Interpretation |
|---|---|---|---|
| Gross Merchandise Value (GMV) | Sum(quantity × unit_price) | All completed orders | Total value of items before discounts, excluding cancelled orders. |
| Net Sales Revenue | Sum(quantity × unit_price × (1 - discount_pct) + shipping_fee) | Completed, non-returned orders | Revenue after discounts, including shipping fees. |
| Orders | Count of distinct order_id | Completed, non-returned orders | Number of completed orders retained by customers. |
| Average Order Value (AOV) | Net sales revenue / retained orders | Completed, non-returned orders | Average revenue generated per retained order. |
| Units Sold | Sum(quantity) | Completed, non-returned orders | Total units retained by customers. |
| Cost of Goods Sold (COGS) | Sum(quantity × unit_cost) | Completed, non-returned orders | Estimated product cost of retained units. |
| Estimated Gross Profit | Net sales revenue - COGS | Completed, non-returned orders | Revenue remaining after product costs, before other expenses. |
| Estimated Gross Margin (%) | (Gross profit / net sales revenue) × 100 | Completed, non-returned orders | Percentage of net sales remaining after product costs. |
| Cancellation Rate (%) | (Cancelled orders / all orders) × 100 | All orders | Percentage of placed orders that were cancelled. |
| Return Rate (%) | (Returned completed orders / completed orders) × 100 | Completed orders | Percentage of completed orders marked as returned. |
| Repeat-Customer Rate (%) | (Customers with 2+ retained orders / customers with 1+ retained orders) × 100 | Customers with completed, non-returned orders | Percentage of purchasing customers who placed multiple orders during the period. |
| Average Discount (%) | Mean(discount_pct) × 100 | Completed, non-returned orders | Average discount percentage applied to retained orders. |
| Marketing Cost per Retained Order | Total attributed marketing cost / retained orders | Completed, non-returned orders | Average attributed marketing cost per retained order. |
| Estimated Contribution After Product and Marketing Costs | Net sales revenue - COGS - attributed marketing cost | Completed, non-returned orders | Estimated contribution after product and attributed marketing costs, excluding other operating expenses. |
| ROAS-like Ratio | Net sales revenue / attributed marketing cost | Retained orders with positive attributed marketing cost | Revenue generated per unit of attributed marketing spend. This is not full ROAS unless marketing spend and attribution are complete. |

## Data requirements and validation checks
Required fields: `order_id`, `order_date`, `customer_id`, `product_category`, `quantity`, `unit_price`, `unit_cost`, `discount_pct`, `shipping_fee`, `order_status`, `is_returned`, `marketing_channel`, `marketing_cost`.

Validation rules:
- `order_id` should be unique and non-null.
- `quantity` must be positive; prices, costs, shipping fees and marketing costs must be non-negative.
- `discount_pct` must be between 0 and 1.
- `order_status` should be one of `Completed` or `Cancelled`.
- Cancelled orders should not be marked returned.
- Dates should parse successfully.
- KPI denominators should be non-zero; otherwise return `NaN`/undefined rather than divide by zero.

## Important limitations
This file does not include website sessions, campaign-level spend, payment fees, fulfillment costs, taxes, inventory availability, or return-value details. Therefore conversion rate, customer acquisition cost (CAC), complete channel ROAS, net profit, and product-level return loss cannot be calculated reliably from this dataset.
