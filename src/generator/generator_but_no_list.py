# Very similar to list comprehension, but using '(' , ')' instead of '[', ']'
gen = (i for i in range(1_000_000_000))
print(gen.__sizeof__())
print(type(gen))