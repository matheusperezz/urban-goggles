n, m = map(int, input().split())
list = []
for i in range(n):
    list.append(int(input()))

list.sort()
list.reverse()
for e in list[:m]:
    print(e)