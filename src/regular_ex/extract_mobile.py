import re


def extract_mobile(string):
    contains_mobile_pattern = r'05\d-?\d{7}'
    match = re.search(contains_mobile_pattern, string)
    if match is not None:
        return string[match.start(): match.end()]
    else:
        return None


string = "hello 052-5958889 my name is Nadav"
print(extract_mobile(string))
