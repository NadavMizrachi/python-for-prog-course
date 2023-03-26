li = [1, 0]
res = True
for i in range(1, len(li)):
    if li[i] < li[i - 1]:
        res = False
        break

print(f"is in ascending order? {res}")

# In list comprehension:
print(all([(li[i] >= li[i - 1]) for i in range(1, len(li))]))
