l1 = [432, 434, 444, 666]

# Notice! sum function getting `generator`, no `list`! Which is much more efficient in terms of memory
ints_sums = map(lambda num: sum(int(dig) for dig in str(num)), l1)

num = 1000
print(type(int(dig) for dig in str(num)))

print(list(ints_sums))