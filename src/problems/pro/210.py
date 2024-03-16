def change_direction(direction):
    if direction == 'c':
        return 'b'
    elif direction == 'd':
        return 'e'
    elif direction == 'b':
        return 'c'
    elif direction == 'e':
        return 'd'

h, w = map(int, input().split())
matrix = []
for _ in range(h):
    row = list(input().strip())
    matrix.append(row)

time = int(input())

while time > 0:
    moved = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            curr = matrix[i][j]
            if curr in ['c', 'd', 'b', 'e'] and not moved[i][j]:
                next_i, next_j = i, j
                if curr == 'c':
                    next_i -= 1
                elif curr == 'd':
                    next_j += 1
                elif curr == 'b':
                    next_i += 1
                elif curr == 'e':
                    next_j -= 1

                if (0 <= next_i < h) and (0 <= next_j < w) and (matrix[next_i][next_j] == 'o'):
                    matrix[next_i][next_j] = curr
                    matrix[i][j] = 'o'
                    moved[next_i][next_j] = True
                else:
                    matrix[i][j] = change_direction(curr)

    time -= 1

for row in matrix:
    print(''.join(row))