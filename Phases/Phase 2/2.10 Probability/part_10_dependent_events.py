# the first event does affect the second.

import numpy as np

box = np.array(["Red"] * 5 + ["Blue"] * 5)

first_draw = np.random.choice(box)

remaining = np.delete(
    box,
    np.where(box == first_draw)[0][0]
)

second_draw = np.random.choice(remaining)

print("First draw:", first_draw)
print("Remaining:", remaining)
print("Second draw:", second_draw)