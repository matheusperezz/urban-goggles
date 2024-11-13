
from math import floor

N = int(input())
nums = list(map(int, input().strip().split()))
p = int(input())

for i in range(N):
    if nums[i] >= p/2:
        print(i, end=" ")
print()
