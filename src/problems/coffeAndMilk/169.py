n = int(input())
items = list(map(int, input().split()))
items.reverse()

for i in items:
    print(i, end=' ')