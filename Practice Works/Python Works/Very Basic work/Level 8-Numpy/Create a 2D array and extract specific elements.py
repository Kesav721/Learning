#Q Create a 2D array and extract specific elements.The first row.The last column.The element at 2nd row and 3rd column


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Element at 2nd row, 3rd column:", arr[1, 2])
