
def smart_div(div_func):
    print("In smarty div... defining inner")
    def inner(n1, n2):
        print("executing inner...")
        if n2 == 0:
            return 0
        else:
            return div_func(n1, n2)
    func_to_return = inner
    print("Returning inner...")
    return func_to_return

@smart_div
def div(a, b):
    print("Executing div...")
    return a / b


print(div(2, 1))
# print(div(2, 0))



