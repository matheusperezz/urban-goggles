n = int(input())
nums = list(map(int, input().split()))
c = int(input())

total = 0
for n in nums:
    if n != c:
        total += n
    else:
        total -= n
print(total)