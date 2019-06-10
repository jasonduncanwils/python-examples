Regex_Pattern = r'\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))