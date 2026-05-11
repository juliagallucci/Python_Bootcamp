import numpy as np

arr = np.array([[2, 7, 12],
                [4, 15, 3],
                [8, 1, 20]])

print("Sum of each column:", np.sum(arr, axis=0))
print("Mean of each row:", np.mean(arr, axis=1))
