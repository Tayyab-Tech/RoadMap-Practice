from part_1_practice_dataset import data

import numpy as np


p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)
p75 = np.percentile(data, 75)
p90 = np.percentile(data, 90)
p95 = np.percentile(data, 95)


print("P25:", p25)
print("P50:", p50)
print("P75:", p75)
print("P90:", p90)
print("P95:", p95)