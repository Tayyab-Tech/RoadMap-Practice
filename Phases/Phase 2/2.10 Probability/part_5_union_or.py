

import numpy as np

S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]     # Even → [2, 4, 6]
B = S[S > 4]          # Greater than 4 → [5, 6]

print("A:", A)
print("B:", B)

union = np.union1d(A, B)

P_union = len(union) / len(S)
print("P(A ∪ B):", P_union)


print("A ∪ B:", union)