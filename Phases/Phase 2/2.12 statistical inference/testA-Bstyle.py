import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Group A
conversions_a = 500
visitors_a = 10_000

# Group B
conversions_b = 560
visitors_b = 10_000

# Conversion rates
rate_a = conversions_a / visitors_a
rate_b = conversions_b / visitors_b

print("A conversion rate:", rate_a)
print("B conversion rate:", rate_b)

# Perform hypothesis test
successes = np.array([conversions_a, conversions_b])
samples = np.array([visitors_a, visitors_b])

z_stat, p_value = proportions_ztest(
    successes,
    samples
)

print("Z-statistic:", z_stat)
print("P-value:", p_value)

# Decision
alpha = 0.05

if p_value < alpha:
    print("Reject H0")
    print("The difference is statistically significant.")
else:
    print("Fail to reject H0")
    print("The difference is not statistically significant.")