Regex_Pattern = r'\d\d\D\d\d\D\d\d\d\d'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))