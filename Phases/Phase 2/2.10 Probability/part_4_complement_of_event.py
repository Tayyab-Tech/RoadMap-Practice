
# Complement means the event does NOT happen.

import numpy as np

S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]      # Even numbers
A_complement = S[S % 2 != 0]   # Not even = Odd

print("A:", A)
print("Aᶜ:", A_complement)

P_A = len(A) / len(S)
P_A_complement = len(A_complement) / len(S)

print("P(A):", P_A)
print("P(Aᶜ):", P_A_complement)