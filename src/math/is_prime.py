num = int(input("Enter number : "))
is_prime = all([(num % d != 0) for d in range(2, num)])
print(is_prime)