n, q = map(int, input().split())
nums = [0 for _ in range(n)]
inputs = list(map(int, input().split()))
for i in range(q):
    mod = inputs[i] % n
    nums[mod] += 1

print(f'Mod {n}')
for i, v in enumerate(nums):
    print(f'{i}: {v}')