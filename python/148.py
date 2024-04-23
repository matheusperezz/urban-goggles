n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n+1):
    idx = nums.index(i)
    print(idx+1, end=' ')

print()
