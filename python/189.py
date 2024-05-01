n = int(input())
nums = list(map(int, input().split()))
m = int(input())

total = 0
for num in nums:

    if total >= m:
        break

    if num == 1:
        total = 0
    elif num > 1:
        total += num

if total >= m:
    print('You Died')
else:
    print('Yes, you can')