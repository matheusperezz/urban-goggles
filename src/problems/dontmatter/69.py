n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(2):
    m = []
    for i in range(n):
        row = list(map(int, input().split()))
        m.append(row)
    
    for i in range(n):
        for j in range(n):
            matrix[i][j] += m[i][j]

for row in matrix:
    for e in row:
        print(e, end=' ')
    print()
        