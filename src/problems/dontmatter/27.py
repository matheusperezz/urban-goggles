points = list(map(float, input().split()))
points.sort()
print(round(sum(points[1:4]), 2))