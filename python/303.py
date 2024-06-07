from math import ceil

siz = 8
Q = [
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
]
matrix = []
for i in range(siz):
    row = list(map(float, input().split()))
    matrix.append(row)

output = []

for i in range(siz):
    row = []
    for j in range(siz):
        val = round(matrix[i][j] / Q[i][j], 0)
        row.append(val)
    output.append(row)

for i in range(siz):
    for j in range(siz):
        print(int(output[i][j]), end=' ')
    print()