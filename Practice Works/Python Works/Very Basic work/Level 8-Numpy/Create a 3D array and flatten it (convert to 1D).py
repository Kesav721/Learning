#Q Create a 3D array and flatten it (convert to 1D)

import numpy as np

arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]],
                  [[9, 10], [11, 12]]])

flat = arr3d.flatten()

print("3D Array:\n", arr3d)
print("Flattened 1D Array:", flat)
