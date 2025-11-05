#Q Create a 3D array and convert it into a base (1D) array

import numpy as np

arr3D = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    
    [[7, 8, 9],
     [10, 11, 12]]
])

print("3D Array:\n", arr3D)

arr1D = arr3D.flatten()
print("\nConverted to 1D Array:\n", arr1D)
