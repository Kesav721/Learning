#Q Extract elements greater than 10 using a loop

import numpy as np

arr = np.array([5, 12, 8, 15, 22, 3])
greater_than_10 = []

for x in arr:
    if x > 10:
        greater_than_10.append(x)

print("Elements greater than 10:", greater_than_10)
