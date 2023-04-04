l1 = [3, -6, 8, 9, -10, 7, -5]

new_li = map(
    lambda num: num if num > 0 else num ** 2,
    l1
)

print(list(new_li))
