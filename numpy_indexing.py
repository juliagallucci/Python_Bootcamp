import numpy as np

arr = np.array([[2, 7, 12],
                [4, 15, 3],
                [8, 1, 20]])

print("First column:", arr[:, 0])
print("Last row:", arr[-1, :])
print("2nd row, 3rd column:", arr[1, 2])
