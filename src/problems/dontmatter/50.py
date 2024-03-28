n = int(input())
nums = list(map(int, input().split()))

mid = 0
for i in range(0, n):
    left = sum(nums[:i])
    right = sum(nums[i:])
    if left == right:
        print(i)
        break