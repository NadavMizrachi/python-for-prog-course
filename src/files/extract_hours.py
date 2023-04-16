import re


def extract_hours(string):
    founds = re.findall("\d\d:\d\d:\d\d" ,string)
    return founds


file_path = r'Z:\___advanced python\01.txt'
string = open(file_path).read()
answer = extract_hours(string)
print(answer)