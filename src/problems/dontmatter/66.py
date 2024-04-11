n, m, a, k = map(int, input().split())
password = input()
is_valid = True

if len(password) < n:
    is_valid = False

num_lowercase = sum(c.islower() for c in password)
if num_lowercase < m:
    is_valid = False

num_uppercase = sum(c.isupper() for c in password)
if num_uppercase < a:
    is_valid = False

num_numeric = sum(c.isdigit() for c in password)
if num_numeric < k:
    is_valid = False

if is_valid:
    print('Ok =/')
else:
    print('Ufa :)')