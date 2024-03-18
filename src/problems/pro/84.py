import bisect

n, m = map(int, input().split())
houses_address = list(map(int, input().split()))
orders = list(map(int, input().split()))
total = 0
prev = 0

for o in orders:
    idx = bisect.bisect_left(houses_address, o)
    total += abs(idx - prev)
    prev = idx

print(total)