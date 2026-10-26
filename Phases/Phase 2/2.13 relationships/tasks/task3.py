
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ==========================================
# PART A — EXPLORE THE DATA
# ==========================================

data = {
    "ad_spend": [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    "website_visits": [500, 650, 800, 950, 1100, 1250, 1400, 1550, 1700, 1850],
    "discount_percent": [0, 5, 0, 10, 5, 15, 10, 5, 20, 10],
    "revenue": [2000, 2400, 3100, 3300, 4000, 4200, 5000, 5100, 6100, 6400]
}

df = pd.DataFrame(data)

print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

print("\nDESCRIPTIVE STATISTICS")
print(df.describe().round(2))

# Correlation matrix
correlation_matrix = df.corr()

print("\nCORRELATION MATRIX")
print(correlation_matrix.round(4))

print("\nCORRELATION WITH REVENUE")
print(
    correlation_matrix["revenue"]
    .drop("revenue")
    .sort_values(ascending=False)
    .round(4)
)

# Scatter plots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

predictors = [
    ("ad_spend", "Advertising Spend"),
    ("website_visits", "Website Visits"),
    ("discount_percent", "Discount Percentage")
]

for ax, (column, label) in zip(axes, predictors):
    ax.scatter(df[column], df["revenue"])
    ax.set_xlabel(label)
    ax.set_ylabel("Revenue")
    ax.set_title(f"{label} vs Revenue")
    ax.grid(True)

plt.tight_layout()
plt.show()


# ==========================================
# PART B — BUILD A MODEL
# ==========================================

X = df[
    ["ad_spend", "website_visits", "discount_percent"]
]

y = df["revenue"]

# Train the multiple linear regression model
model = LinearRegression()
model.fit(X, y)

# Display the regression equation
print("\nREGRESSION MODEL")

print("Intercept:", round(model.intercept_, 4))

for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature} coefficient: {coefficient:.4f}")

# Predict revenue for the existing observations
predictions = model.predict(X)

# Compare actual and predicted revenue
comparison = pd.DataFrame({
    "actual_revenue": y,
    "predicted_revenue": predictions,
    "error": y - predictions
})

print("\nACTUAL VS PREDICTED REVENUE")
print(comparison.round(2))

# Evaluate model performance
r2 = r2_score(y, predictions)
mae = mean_absolute_error(y, predictions)
rmse = np.sqrt(mean_squared_error(y, predictions))

print("\nMODEL EVALUATION")
print("R-squared:", round(r2, 4))
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))

# Plot actual vs predicted revenue
plt.figure(figsize=(7, 5))

plt.scatter(y, predictions, label="Observations")

min_value = min(y.min(), predictions.min())
max_value = max(y.max(), predictions.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Revenue")
plt.ylabel("Predicted Revenue")
plt.title("Actual vs Predicted Revenue")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ==========================================
# PART C — PROFESSIONAL REPORT
# ==========================================

print("\nPROFESSIONAL REPORT")

print(
    "Advertising spend and website visits have the "
    "strongest observed positive linear associations with revenue."
)

print(
    f"The model's in-sample R-squared is {r2:.4f}."
)

print(
    "These associations do not establish causation. "
    "More data and a suitable causal study design are needed."
)
