n = int(input())
total = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    dist = ((x2 - x1)**2) + ((y2-y1)**2)
    total += dist

print(total)