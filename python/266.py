import re

def replace_and_count(match):
    return '@' + str(len(match.group()))

n = input()
n = re.sub(r'0+', replace_and_count, n)
print(n)