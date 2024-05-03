from bisect import bisect_left

rounds = int(input())
outputs = []
for _ in range(rounds):
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    outputs.append(bisect_left(nums, k))
    
for o in outputs:
    print(o)
