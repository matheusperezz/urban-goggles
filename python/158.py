n = int(input())
nums = list(map(int, input().split()))
nums.sort()
for num in nums[:8]:
    print(num, end=' ')
print()