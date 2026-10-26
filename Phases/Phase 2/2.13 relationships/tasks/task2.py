import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create the dataset
data = {
    "ad_spend": [100, 200, 300, 400, 500, 600, 700, 800],
    "sales": [1200, 1500, 1900, 2100, 2600, 2900, 3100, 3600]
}

df = pd.DataFrame(data)

# 2. Calculate correlation
correlation = df["ad_spend"].corr(df["sales"])

print("Pearson Correlation:", round(correlation, 4))

# 3. Fit the linear regression model using NumPy
slope, intercept = np.polyfit(
    df["ad_spend"],
    df["sales"],
    1
)

print("Slope:", round(slope, 4))
print("Intercept:", round(intercept, 4))

# 4. Predict sales for advertising spend of 450
ad_spend = 450
predicted_sales = slope * ad_spend + intercept

print("Predicted Sales:", round(predicted_sales, 2))

# 5. Generate regression line values
predicted_values = slope * df["ad_spend"] + intercept

# 6. Plot observed data and regression line
plt.figure(figsize=(8, 5))

plt.scatter(
    df["ad_spend"],
    df["sales"],
    label="Observed Sales",
    marker="o"
)

plt.plot(
    df["ad_spend"],
    predicted_values,
    label="Regression Line"
)

plt.xlabel("Advertising Spend")
plt.ylabel("Sales Revenue")
plt.title("Advertising Spend vs Sales Revenue")
plt.legend()
plt.grid(True)

plt.show()