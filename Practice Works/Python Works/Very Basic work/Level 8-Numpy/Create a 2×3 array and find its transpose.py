#Q Create a 2×3 array and find its transpose

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

transpose = arr.T
print("Original:\n", arr)
print("\nTranspose:\n", transpose)
