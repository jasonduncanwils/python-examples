Regex_Pattern = r'^[\d]{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))