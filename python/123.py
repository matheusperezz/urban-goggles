def verify(matrix, i, j):
    if matrix[i+1][j] == matrix[i-1][j] == matrix[i][j+1] == matrix[i][j-1] == 1:
        return (i, j)
    return (0, 0)

n, m = map(int, input().split())
matrix = []
is_eliminated = (0, 0)
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            is_eliminated = verify(matrix, i, j)

print(f'{is_eliminated[0]} {is_eliminated[1]}')
