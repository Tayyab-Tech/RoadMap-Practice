import numpy as np
# An event is a specific outcome or a collection of outcomes from the sample space that we are interested in.
# We usually represent events using:
# A, B, C
# We call this Event A - even number:
# A = {2, 4, 6}
# Event B — Odd number
# B = {1, 3, 5}
# Event C — Number greater than 4
# C = {5, 6}


S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]

print("Event A:", A)
print("P(A):", len(A) / len(S))


B = S[S % 2 != 0]

print("Event B:", B)
print("P(B):", len(B) / len(S))


C = S[S > 4]

print("Event C:", C)
print("P(C):", len(C) / len(S))