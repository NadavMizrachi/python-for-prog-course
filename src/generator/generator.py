# Generator is function that yields int in each call.
def gener(n):
    i = 0
    while i < n:
        yield i
        i += 1

# We can iterate with for on generator

for i in gener(10):
    print(i)