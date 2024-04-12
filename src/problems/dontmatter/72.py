n = int(input())
matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

# Percorrendo
i = 0
j = 0
points = 0
results = []
while i < n:
    e = matrix[i][j]
    if e == 'o':
        points += 1
    elif e == 'A':
        results.append(points)
        points = 0

    results.append(points)

    if i % 2 == 0:
        j += 1
    else:
        j -= 1

    if j == n:
        i += 1
        j = n-1
    elif j == -1:
        i += 1
        j = 0
    
results.append(points)
print(max(results))