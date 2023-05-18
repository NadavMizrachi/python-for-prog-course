import random

import matplotlib.pyplot as plt

fig = plt.figure()
x = ['a', 'b', 'c', 'd']
y = [random.randint(10, 20) for i in range(4)]
plt.plot(x, y)
plt.show()

