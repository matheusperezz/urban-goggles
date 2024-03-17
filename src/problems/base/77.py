n, m = map(int, input().split())
times = []
for i in range(n):
    laps = sum(map(int, input().split()))
    times.append(laps)

indexed_list = list(enumerate(times))
sorted_list = sorted(indexed_list, key=lambda x: x[1])
podium = sorted_list[:3]

for i in podium:
    print(i[0]+1)
