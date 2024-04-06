matriz = []
size = 8
for _ in range(size):
    row = list(map(int, input().split()))
    matriz.append(row)

i, j = 0, 0
while True:
    print(matriz[i][j])
    