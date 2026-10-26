from part_1_practice_dataset import data

import numpy as np


def statistics_report(data):

    mean = np.mean(data)
    median = np.median(data)

    variance = np.var(data)
    standard_deviation = np.std(data)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    outliers = data[
        (data < lower_bound) |
        (data > upper_bound)
    ]

    print("Mean:", mean)
    print("Median:", median)
    print("Variance:", variance)
    print("Standard Deviation:", standard_deviation)
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Outliers:", outliers)


statistics_report(data)



# The median represents the typical observation better than the mean because the dataset contains a high-value outlier. The standard deviation indicates substantial variability, while the IQR shows the spread of the middle 50% of observations. Using the 1.5 × IQR rule, the extreme value is flagged as a potential outlier.