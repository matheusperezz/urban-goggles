import math

n = int(input())
max_val = -1
max_index = -1

for i in range(n):
    d, c = map(int, input().split())
    val = c * math.log(d)
    if val > max_val:
        max_val = val
        max_index = i

print(max_index)