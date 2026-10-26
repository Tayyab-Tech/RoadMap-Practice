import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "category": [
        "Electronics", "Clothing", "Electronics", "Books",
        "Clothing", "Books", "Electronics", "Clothing",
        "Books", "Electronics"
    ],
    "region": [
        "Lahore", "Karachi", "Lahore", "Islamabad",
        "Karachi", "Lahore", "Islamabad", "Lahore",
        "Karachi", "Lahore"
    ],
    "sales": [5000, 1200, 7500, 800, 1800, 600, 9000, 1500, 700, 6500],
    "discount": [5, 10, 0, 5, 15, 0, 10, 5, 0, 20],
    "quantity": [2, 3, 1, 4, 2, 5, 1, 3, 4, 2]
}

df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())



plt.figure(figsize=(8, 5))

# sns.histplot(data=df, x="sales", bins=5, kde=True)

# plt.title("Distribution of Order Sales")
# plt.xlabel("Sales")
# plt.ylabel("Number of Orders")
# plt.tight_layout()
# plt.show()



# sns.boxplot(data=df, x="sales")

# plt.title("Sales Spread and Potential Outliers")
# plt.xlabel("Sales")
# plt.show()



print("Mean:", df["sales"].mean())
print("Median:", df["sales"].median())
print("Standard deviation:", df["sales"].std())
print("25th percentile:", df["sales"].quantile(0.25))
print("75th percentile:", df["sales"].quantile(0.75))
print("Minimum:", df["sales"].min())
print("Maximum:", df["sales"].max())


# Written insight template:
# Order sales are concentrated in [observed range]. The mean is [value], while the median is [value], suggesting [interpretation]. This matters because [business implication]. However, [limitation or additional check].






# 5. Segment analysis
# Segment analysis means dividing data into groups and comparing their performance.

# For example, an online store might want to know which product category generates the most revenue.
# A. Compare sales by category

category_sales = (
    df.groupby("category")["sales"]
      .agg(["count", "sum", "mean", "median"])
      .sort_values("sum", ascending=False)
)

print(category_sales)



# B. Compare regions

region_sales = (
    df.groupby("region")
      .agg(
          total_sales=("sales", "sum"),
          average_order=("sales", "mean"),
          order_count=("order_id", "count")
      )
      .sort_values("total_sales", ascending=False)
)

print(region_sales)


# Plot the results:

# sns.barplot(
#     data=df,
#     x="region",
#     y="sales",
#     estimator="sum",
#     errorbar=None
# )

# plt.title("Total Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Total Sales")
# plt.tight_layout()
# plt.show()



# C. Segment by two variables
# You can also compare categories across regions.


print("\nSegment Table: Sales by Category and Region")
segment_table = pd.pivot_table(
    df,
    index="category",
    columns="region",
    values="sales",
    aggfunc="sum",
    fill_value=0
)

print(segment_table)


# sns.heatmap(segment_table, annot=True, fmt=".0f", cmap="YlGnBu")

# plt.title("Sales by Category and Region")
# plt.xlabel("Region")
# plt.ylabel("Category")
# plt.tight_layout()
# plt.show()



# 6. Relationship analysis
# A relationship analysis investigates how variables change together.

# For this lesson, we'll examine three types.
# A. Numerical versus numerical: scatter plot
# Business question: Do higher discounts correspond to higher sales?


# sns.scatterplot(
#     data=df,
#     x="discount",
#     y="sales",
#     hue="category",
#     s=100
# )

# plt.title("Discount vs Sales")
# plt.xlabel("Discount (%)")
# plt.ylabel("Order Sales")
# plt.tight_layout()
# plt.show()


print("\nCorrelation Table: Sales, Discount, and Quantity")
# Correlation in Python:
print(df[["sales", "discount", "quantity"]].corr())






# B. Categorical versus numerical: box plot
# Business question: Do order values differ across product categories?


# sns.boxplot(
#     data=df,
#     x="category",
#     y="sales"
# )

# plt.title("Order Sales by Category")
# plt.xlabel("Category")
# plt.ylabel("Sales")
# plt.tight_layout()
# plt.show()


# C. Categorical versus categorical: cross-tabulation
# Business question: Which categories appear most often in each region?

print("\nCross-tabulation: Category Counts by Region")
counts = pd.crosstab(df["region"], df["category"])
print(counts)

# For proportions within each region:
print("\nProportions: Category Distribution by Region")
proportions = pd.crosstab(
    df["region"],
    df["category"],
    normalize="index"
) * 100

print(proportions.round(1))


# 7. Discover patterns over time
# Real EDA often includes dates. If your dataset has an order date, first convert it to a datetime type.

# df["order_date"] = pd.to_datetime(df["order_date"])

# df["month"] = df["order_date"].dt.to_period("M")

# monthly_sales = df.groupby("month")["sales"].sum()

# monthly_sales.plot(kind="line", marker="o")

# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.tight_layout()
# plt.show()



