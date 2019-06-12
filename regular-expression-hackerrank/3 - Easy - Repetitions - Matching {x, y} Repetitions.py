Regex_Pattern = r'^[\d]{1,2}[a-zA-Z]{3,}[\.]{,3}$'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))