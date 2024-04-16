n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = [x for x in nums if x != 0]

for idx in range(len(nums) - m, len(nums)):
    print(nums[idx], end=" ")

print()
