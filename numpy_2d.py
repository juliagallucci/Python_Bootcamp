import numpy as np

arr = np.array([[2, 7, 12],
                [4, 15, 3],
                [8, 1, 20]])

print("Elements greater than 10:", arr[arr > 10])

arr[arr < 5] = 0
print("Array after replacing elements less than 5 with 0:\n", arr)
