from part_1_practice_dataset import data

import numpy as np


q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1


print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)