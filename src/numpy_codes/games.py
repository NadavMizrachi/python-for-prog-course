import numpy as np

arr = np.arange(18)
arr = arr.reshape(3, 6)
print(arr)
print(arr[::2, 3:5])
# 3 4 15 16