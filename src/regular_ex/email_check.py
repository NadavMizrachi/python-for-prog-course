import re


def is_valid_email(string):
    email_pattern = r'^\w@\w.\w'
    return re.search(email_pattern, string) is not None


e1 = "nadav16@gmail.com"
print(f"{e1} = {is_valid_email(e1)}")

e2 = "nadav16@gmail"
print(f"{e2} = {is_valid_email(e2)}")

e3 = "nadav16 aa@gmail.com"
print(f"{e3} = {is_valid_email(e3)}")

e4 = "nadav16 @gmail.com"
print(f"{e4} = {is_valid_email(e4)}")

e5 = "@gmail.com"
print(f"{e5} = {is_valid_email(e5)}")

e6 = "gmail.com"
print(f"{e6} = {is_valid_email(e6)}")
