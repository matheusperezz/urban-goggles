n, m = map(int, input().split())
stones = [0 for _ in range(n)]
for _ in range(m):
    position, jump_distance = map(int, input().split())
    current_pos = position-1
    stones[current_pos] = 1

    # Right jumps
    for i in range(current_pos + jump_distance, n, jump_distance):
        if i < n:
            stones[i] = 1
        else:
            break

    # Left jumps
    for i in range(current_pos - jump_distance, -1, -jump_distance):
        if i >= 0:
            stones[i] = 1
        else:
            break

for s in stones:
    print(s)
