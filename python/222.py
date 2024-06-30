n = int(input())
nums= list(map(int, input().split(" ")))
d = {}
for num in nums:
    if num in d.keys():
        d[num] += 1
    else:
        d[num] = 1

T = []
for k, v in d.items():
    if v == 3:
        T.append(k)

T.sort()
c = 0
for t in T:
    if c == 3: break
    print(t, end=' ')
print()