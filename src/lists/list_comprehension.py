nums = [1, 2, 3, 4, 5, 6, 7]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(f" From {nums} ... the evens are: {evens}")

# In list comprehension:
evens = [num for num in nums if num % 2 == 0]

print(f" In list comprehension -> From {nums} ... the evens are: {evens}")


print(f" one to ten powers: { [num**2 for num in range(1,11)] }")