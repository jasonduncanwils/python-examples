import re

n = int(input())
sentences = '\n'.join([input().strip().replace('_','') for _ in range(n)])
for _ in range(int(input())):
    wd = input().strip()
    pattern = r'(\W|\b)'+ wd +'(\W|\b)'
    match_count = re.findall(pattern,sentences)
    print(len(match_count))