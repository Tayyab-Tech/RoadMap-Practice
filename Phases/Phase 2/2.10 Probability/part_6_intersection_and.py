

import numpy as np

S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]     # Even → [2, 4, 6]
B = S[S > 4]          # Greater than 4 → [5, 6]


intersection = np.intersect1d(A, B)

print("A ∩ B:", intersection)


P_intersection = len(intersection) / len(S)

print("P(A ∩ B):", P_intersection)