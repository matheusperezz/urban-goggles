n = int(input())
output = 0
for _ in range(n):
    val = int(input())
    if val % 3 == 0:
        output += val + 50
    else:
        output += val / 2

print(int(output))
