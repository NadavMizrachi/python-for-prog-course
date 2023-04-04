import re

string = '90hello'

starts_with_pattern = "^he"
starts_with_match_obj = re.search(starts_with_pattern, string)
print(starts_with_match_obj)

ends_with_pattern = "lo$"
ends_with_match_obj = re.search(ends_with_pattern , string)
print(ends_with_match_obj)

zero_or_one_pattern = "lo$"
ends_with_match_obj = re.search(ends_with_pattern , string)
print(ends_with_match_obj)


# Split by regex
text = 'one is 1, two is 2'
split_text = re.split('[, ]+', text)
print(split_text)
