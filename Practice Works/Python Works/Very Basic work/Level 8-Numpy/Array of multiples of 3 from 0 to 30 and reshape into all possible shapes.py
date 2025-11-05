#Q Array of multiples of 3 from 0 to 30 and reshape into all possible shapes

import numpy as np

arr=np.arange(0,31,3)
print("array :",arr)

reshape1 = arr.reshape(1, 11)
reshape2 = arr.reshape(11, 1)

print("Shape (1x11):\n", reshape1)
print("Shape (11x1):\n", reshape2)
