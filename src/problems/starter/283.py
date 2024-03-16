l, c = map(int, input().split())
matrix = []
for _ in range(l):
    row = list(map(int, input().strip().split()))
    matrix.append(row)

queue, a1, a2 = 0, 0, 0
for i in range(l):
    for j in range(c):
        if matrix[i][j] == 0 and j+1 < c:
            if matrix[i][j+1] == 0:
                queue = i+1
                a1, a2 = j+1, j+2

print(f'Fileira: {queue}')
print(f'Assentos: {a1} e {a2}')