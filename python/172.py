n, e = map(int, input().split())
day = []
for i in range(n):
    val = int(input())
    e -= val
    if e <= 0:
        day.append(i+1)

if len(day) == 0:
    print('Resistiu')
else:
    print(day[0])