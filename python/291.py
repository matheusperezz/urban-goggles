n = int(input())
nums = list(map(int, input().split()))

for i in range(n, 0, -1):
    print(f'{i}: {nums[i-1]}')