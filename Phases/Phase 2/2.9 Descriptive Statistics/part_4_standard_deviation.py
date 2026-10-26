from part_1_practice_dataset import data

import numpy as np


population_std = np.std(data)

sample_std = np.std(data, ddof=1)


print("Population Standard Deviation:", population_std)
print("Sample Standard Deviation:", sample_std)