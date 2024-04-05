def solve(c):
    if c.isdigit():
        return c
    elif c == '-':
        return c
    mapping = {'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL': '5', 'MNO': '6', 'PQRS': '7', 'TUV': '8', 'WXYZ': '9'}
    for key in mapping:
        if c in key:
            return mapping[key]

s = input()
result = ''.join(solve(letter) for letter in s)
print(result)