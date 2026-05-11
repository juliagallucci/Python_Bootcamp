import numpy as np

arr = np.arange(9)
arr = arr.reshape((3, 3))
result = arr % 1 == 0

print(result)
