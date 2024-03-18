import math
import bisect

c, t = map(int, input().split())
radius = [int(input()) for _ in range(c)]
points, total_point = 0, len(radius)
for j in range(t):
    x, y = map(int, input().split())
    d = math.sqrt(x**2 + y**2)
    if d <= radius[0]:
        points += total_point
    elif d > radius[-1]:
        points += 0
    else:
        point = total_point - bisect.bisect_left(radius, d)
        points += point

print(points)