def solve(string):
    size = len(string)
    for i in range(1, size // 2 + 1):
        if size % i == 0:
            substring = string[:i]
            if substring * (size // i) == string:
                return True
    return False

s = input().strip()

if solve(s):
    print("VALIDO")
else:
    print("INVALIDO")
