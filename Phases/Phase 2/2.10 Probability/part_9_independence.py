# Two events are independent when one does not affect the other.
# For example, flipping a coin twice.

import numpy as np

flips = np.random.choice(["Heads", "Tails"], size=10000)

print(flips[:10])


# For two separate coin flips, the result of the first flip doesn't change the probability of the second.

# For independent events:

# P(A∩B)=P(A)×P(B)