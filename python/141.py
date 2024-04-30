def calc(matrix, m, n):
    mincost = [[0] * n for _ in range(m)]
    mincost[0] = matrix[0]
    for i in range(1, m):
        for j in range(n):
            currcost = matrix[i][j]
            if j == 0:
                mincost[i][j] = currcost + min(mincost[i-1][j], mincost[i-1][j+1])
            if j == n - 1:
                mincost[i][j] = currcost + min(mincost[i-1][j-1], mincost[i-1][j])
            else:
                mincost[i][j] = currcost + min(mincost[i-1][j-1], mincost[i-1][j], mincost[i-1][j+1])

    result = min(mincost[0])
    return result

m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

r = calc(matrix, m, n)
print(r)
