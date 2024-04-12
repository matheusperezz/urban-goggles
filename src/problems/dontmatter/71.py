def verify_sides(matrix, i, j, n, m):
    is_coast = False

    if (i == n-1 or j == m-1) and matrix[i][j] == '#':
        return True

    if matrix[i][j] == '#':
        if i+1 < n and matrix[i+1][j] != '#':
            is_coast = True
        if i-1 >= 0 and matrix[i-1][j] != '#':
            is_coast = True
        if j+1 < m and matrix[i][j+1] != '#':
            is_coast = True
        if j-1 < m and matrix[i][j-1] != '#':
            is_coast = True
    
    return is_coast


n, m = map(int, input().split())
matrix = []
output = 0
for i in range(n):
    row = list(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        if verify_sides(matrix, i, j, n, m):
            output += 1

print(output)