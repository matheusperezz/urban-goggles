n, m = map(int, input().strip().split())
dms = list(map(int, input().strip().split()))
pssb = list(map(int, input().strip().split()))
count = 0

for p in pssb:
    if p in dms:
        count += 1

print(count)