import numpy as np

mat = np.arange(12).reshape((3, 4))
print(mat)
rows = np.array([2, 2, 1, 1])
colms = np.array([0, 1, 0, 1])

print(np.array(mat[rows, colms]).reshape(2, 2))
