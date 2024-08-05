N = 8
matrix = []
for i in range(N):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

for i in range(N):
    for j in range(N):
        matrix[i][j] -= 128
        print(matrix[i][j], end=' ')
    print()