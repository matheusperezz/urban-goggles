matriz = []
size = 8
for _ in range(size):
    row = list(map(int, input().split()))
    matriz.append(row)

linhas, colunas = 8, 8
for i in range(linhas + colunas - 1):
    diagonal = []
    for j in range(max(0, i - linhas + 1), min(i + 1, colunas)):
        diagonal.append(matriz[i - j][colunas - j - 1])
    for d in diagonal:
        print(d, end=' ')