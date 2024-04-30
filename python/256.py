n = int(input())
nums = []
for _ in range(n):
    val = int(input())
    nums.append(val)

nums.sort()
for num in nums:
    print(num, end=' ')
print()
