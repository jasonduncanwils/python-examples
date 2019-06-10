Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][\.,]$'	# Do not delete 'r'.

import re
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))