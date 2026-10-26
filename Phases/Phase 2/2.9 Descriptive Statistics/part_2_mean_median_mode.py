from part_1_practice_dataset import data
from scipy import stats
import numpy as np


mean = np.mean(data)
print("Mean:", mean)


median = np.median(data)
print("Median:", median)

mode = stats.mode(data, keepdims=True)
print("Mode:", mode.mode[0])