n = int(input())
nums = list(map(int, input().split()))
median = sum(nums) / n
count = 0
for num in nums:
    if num > median:
        count += 1

print(count)