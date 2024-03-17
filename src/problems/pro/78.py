n, k = map(int, input().split())
list = []
for i in range(n):
    list.append(input())

list.sort()
print(list[k-1])