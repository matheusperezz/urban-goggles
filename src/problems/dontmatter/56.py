size, target = map(int, input().split())
nums = list(map(int, input().split()))
occr = {}
for n in nums:
    if n in occr:
        occr[n] += 1
    else:
        occr[n] = 1

if len(occr) == target:
    print(min(occr.values()))
else:
    print(0)