Regex_Pattern = r'\S\S\s\S\S\s\S\S'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))