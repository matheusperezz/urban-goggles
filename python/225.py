n = int(input())
used = list(map(int, input().split()))
hited = list(map(int, input().split()))

for i in range(n):
    if used[i] == 0:
        print(0, end=' ')
    else:
        val = (hited[i]/used[i]) * 100
        print(int(val), end=' ')

print()
