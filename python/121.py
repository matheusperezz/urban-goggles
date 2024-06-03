n = int(input())
nums = list(map(int, input().split()))
output = [nums[0]]
for i in range(1, n):
    val = nums[i] - nums[i-1]
    output.append(val)

for o in output:
    print(o, end=' ')
print()
