n = int(input())
nums = list(map(int, input().split()))
c = int(input())
is_finded = False
for num in nums:
    if num == c:
        is_finded = True
        break

if is_finded:
    print(c)
else:
    print(-1)