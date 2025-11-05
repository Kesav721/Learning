#Q .Create two 2d arrays and perform element-wise addition, subtraction, multiplication,division and dot product.

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("Addition :\n",A+B)
print("Subtraction :\n",A-B)
print("Multiplication :\n",A*B)
print("Division :\n",A/B)
print("Dot Product :\n",np.dot(A, B))
