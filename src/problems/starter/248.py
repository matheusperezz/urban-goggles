MATRIX_SIZE = int(input())

matrix = []
for _ in range(MATRIX_SIZE):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

tree_total = 0
n_cordenates = int(input())
for i in range(n_cordenates):
    x, y = map(int, input().split())
    tree_total += matrix[x][y]

print(tree_total)