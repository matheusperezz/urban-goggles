def decrease(nums) -> int:
    total = nums[0]
    decs = [x*-1 for x in nums[1:]]
    total = total + sum(decs)
    return total

n = int(input())
age = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    s = sum(nums)
    if s >= 100:
        age += decrease(nums)
    else:
        age += s

print(f'{age} anos de vida')