n = int(input())
cups = []
for _ in range(n):
    x, y = map(int, input().split())
    cups.append(x)
    cups.append(y)

total = 0
for i in range(0, len(cups), 2):
    if cups[i] > cups[i+1]:
        total += cups[i+1]

print(total)