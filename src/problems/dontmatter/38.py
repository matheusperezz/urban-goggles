n = int(input())
total = 0
for _ in range(n):
    x, y = map(int, input().split())
    total += x*y

print(total)