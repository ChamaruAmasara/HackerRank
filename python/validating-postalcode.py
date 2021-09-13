#https://www.hackerrank.com/challenges/validating-postalcode/problem

regex_integer_in_range = r"[1-9][0-9][0-9][0-9][0-9][0-9]"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=((\d)\d\2))"	# Do not delete 'r'.


import re
P = input()
print((re.findall(regex_alternating_repetitive_digit_pair, P)))
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)