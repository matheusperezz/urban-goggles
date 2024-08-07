def calc(matrix, m, n):
    mincost = [[0] * n for _ in range(m)]
    mincost[m-1] = matrix[m-1]
    for i in range(m-2, -1, -1):
        for j in range(n):
            currcost = matrix[i][j]
            if j == 0:
                mincost[i][j] = currcost + min(mincost[i+1][j], mincost[i+1][j+1])
            elif j == n - 1:
                mincost[i][j] = currcost + min(mincost[i+1][j-1], mincost[i+1][j])
            else:
                mincost[i][j] = currcost + min(mincost[i+1][j-1], mincost[i-1][j], mincost[i+1][j])

    result = min(mincost[0])
    return result

m, n = map(int, input().split())
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

r = calc(matrix, m, n)
print(r)
