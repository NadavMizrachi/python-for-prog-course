def cap_first_letter(word):
    return word[0:1].upper() + word[1:]


user_input = input("Enter your name : ")
full_name = user_input.split()
print(cap_first_letter(full_name[0] + " " + cap_first_letter(full_name[1])))

# Second way :
print(f"{full_name[0].capitalize()} {full_name[1].capitalize()}")


