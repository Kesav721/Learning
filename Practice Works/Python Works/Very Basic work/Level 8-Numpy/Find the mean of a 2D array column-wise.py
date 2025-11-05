#Q Find the mean of a 2D array column-wise

import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

mean_col = np.mean(arr, axis=0)
print("Column-wise mean:", mean_col)
