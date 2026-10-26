# Conditional probability means:

# Probability of A given that B has already happened.

# Written:

# P(A|B)

# The formula is:

# P(A∣B)=P(A∩B)/P(B)


import numpy as np
import pandas as pd

S = np.array([1, 2, 3, 4, 5, 6])

A = S[S % 2 == 0]
B = S[S > 4]

intersection = np.intersect1d(A, B)

P_intersection = len(intersection) / len(S)
P_B = len(B) / len(S)

P_A_given_B = P_intersection / P_B

print("A:", A)
print("B:", B)
print("A ∩ B:", intersection)
print("P(A | B):", P_A_given_B)




# with the help of pandas 

data = {
    "Gender": ["Male", "Male", "Male", "Male", "Female", "Female"],
    "Result": ["Passed", "Passed", "Failed", "Passed", "Passed", "Failed"]
}

df = pd.DataFrame(data)

# print(df)

males = df[df["Gender"] == "Male"]
print(males)


passed_males = (males["Result"] == "Passed").sum()

total_males = len(males)

probability = passed_males / total_males

print(probability)
