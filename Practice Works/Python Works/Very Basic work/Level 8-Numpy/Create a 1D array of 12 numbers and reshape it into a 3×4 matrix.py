#Q Create a 1D array of 12 numbers and reshape it into a 3×4 matrix.

import numpy as np

arr= np.array([10,20,30,40,50,60,70,80,90,100,110,120])

reshaped= arr.reshape(2,6)

print(reshaped)
  
