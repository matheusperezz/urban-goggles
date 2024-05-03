
n, m = map(int, input().split())
nums = list(map(int, input().split()))
out = [x for x in range(1, n+1)]

for num in out:
  if num not in nums:
    print(num, end=' ')

print()