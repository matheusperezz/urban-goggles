n = int(input())
s = input()
total = 0
for c in s:
    if c == 'P':
        total += 2
    elif c == 'C':
        total += 2
    elif c == 'A':
        total += 1

print(total)
    