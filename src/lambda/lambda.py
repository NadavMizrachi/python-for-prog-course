

# Callable - Function with name that we can use later
def pow(num):
    return num ** 2

func_container = pow

print(f"func_container(2) = {func_container(2)}")


# Lambda - Function defined in place
is_even_lmbda = lambda num: num % 2 == 0

in_li = list(range(0, 10))

even_numbers = filter(is_even_lmbda, in_li)
print(list(even_numbers))



