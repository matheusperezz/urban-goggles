n, m = input().split()
n = int(n)
m = float(m)
idx, total = [], 0
for i in range(n):
    val = float(input())
    total += val
    if total >= m and len(idx) <= 1:
        total -= m
        idx.append(i+1)

total = "{:.2f}".format(total)
if len(idx) == 0:
    print(f'0 {total}')
else:
    print(f'{idx[0]} {total}')