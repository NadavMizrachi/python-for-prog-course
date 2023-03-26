user_input = input("Enter text: ")

print({char: user_input.count(char) for char in user_input})
