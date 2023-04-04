from functools import reduce

l1 = list(range(0, 11))

print(reduce(lambda x, y: y, l1))
