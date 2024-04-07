frogs, stones = map(int, input().split())
available_stones = [0 for _ in range(stones)]
for _ in range(frogs):
    jump_dist = int(input())
    for i in range(0, stones, jump_dist):
        available_stones[i] = 1

for a in available_stones:
    print(a, end=' ')
