# Question: A coin has two possible outcomes:

# Heads
# Tails

# What is the probability of getting Heads?
# P(Heads)=​1/2=0.5

# Because:

# Favorable outcomes = 1 (Heads)
# Total outcomes = 2 (Heads, Tails)




import numpy as np
flips = np.random.choice(["Heads", "Tails"], size=10000)
heads_count = np.sum(flips == "Heads")
probability = heads_count / len(flips)
print(probability)