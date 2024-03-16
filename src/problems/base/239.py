MATRIX_SIZE = 10

matrix = []
for _ in range(MATRIX_SIZE):
    row = input().strip().split()
    matrix.append(row)

for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        # Up
        if j-1 >= 0 and matrix[i][j] == 't' and matrix[i][j-1] == '*':
            matrix[i][j] = 'p'
        # Down
        if j+1 < MATRIX_SIZE and matrix[i][j] == 't' and matrix[i][j+1] == '*':
            matrix[i][j] = 'p'
        # Left
        if i-1 >= 0 and matrix[i][j] == 't' and matrix[i-1][j] == '*':
            matrix[i][j] = 'p'    
        # Right
        if i+1 < MATRIX_SIZE and matrix[i][j] == 't' and matrix[i+1][j] == '*':
            matrix[i][j] = 'p'


for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        print(f'{matrix[i][j]}', end=' ')
    print()