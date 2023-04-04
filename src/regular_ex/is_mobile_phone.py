import re

mobile_pattern = r'^05\d-?\d{7}$'


def is_mobile_phone(string):
    return re.search(mobile_pattern, string) is not None

if __name__ == "__main__":
    # Good
    print(is_mobile_phone("0525958889"))
    print(is_mobile_phone("052-5958889"))

    # Bad
    print(is_mobile_phone("0525-958889"))
    print(is_mobile_phone("0525958d89"))
    print(is_mobile_phone("525958889"))
    print(is_mobile_phone("0525958889888"))
    print(is_mobile_phone("1110525958889"))
