Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))