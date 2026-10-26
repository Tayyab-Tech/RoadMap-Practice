from part_1_practice_dataset import data

import numpy as np


population_variance = np.var(data)
sample_variance = np.var(data, ddof=1)


print("Population Variance:", population_variance)
print("Sample Variance:", sample_variance) 