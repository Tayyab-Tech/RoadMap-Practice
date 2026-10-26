# The addition rule is:

# P(A∪B)=P(A)+P(B)−P(A∩B)


import numpy as np

S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]
B = S[S > 4]

P_A = len(A) / len(S)
P_B = len(B) / len(S)

intersection = np.intersect1d(A, B)
P_intersection = len(intersection) / len(S)

P_union = P_A + P_B - P_intersection

print("P(A):", P_A)
print("P(B):", P_B)
print("P(A ∩ B):", P_intersection)
print("P(A ∪ B):", P_union)