# A fair six-sided die is rolled once.

# Calculate:

# Probability of getting an even number.
# Probability of getting a number greater than 4.
# Probability of getting an odd number.
# Probability of not getting 6.


import numpy as np

# Sample space
die = np.array([1, 2, 3, 4, 5, 6])

# 1. P(Even)
even = die[die % 2 == 0]
p_even = len(even) / len(die)

# 2. P(number > 4)
greater_4 = die[die > 4]
p_greater_4 = len(greater_4) / len(die)

# 3. P(Odd)
odd = die[die % 2 != 0]
p_odd = len(odd) / len(die)

# 4. P(Not 6)
p_not_6 = np.sum(die != 6) / len(die)

print("P(Even):", p_even)
print("P(>4):", p_greater_4)
print("P(Odd):", p_odd)
print("P(Not 6):", p_not_6)