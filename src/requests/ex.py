import requests
import re


def extract_phones(text):
    phone_pattern = r'0\d-?\d{7}'
    return re.findall(phone_pattern, text)


response = requests.get("https://www.rehovot.muni.il/phonebook/")

csv = open('phones.csv' , 'w')
csv.write("PHONE\n")
for phone_num in extract_phones(response.text):
    csv.writelines(phone_num + "\n")