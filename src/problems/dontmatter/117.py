n = int(input())
nums = list(map(int, input().split()))
mlt = int(input())
nums = [x * mlt for x in nums]
for num in nums:
    print(num, end=" ")
