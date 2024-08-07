def zigzag_scan(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    row, col = 0, 0
    up = True

    for _ in range(rows * cols):
        result.append(matrix[row][col])
        
        if up:
            if col == cols - 1:
                row += 1
                up = False
            elif row == 0:
                col += 1
                up = False
            else:
                row -= 1
                col += 1
        else:
            if row == rows - 1:
                col += 1
                up = True
            elif col == 0:
                row += 1
                up = True
            else:
                row += 1
                col -= 1

    return result

matrix = []
for _ in range(8):
    matrix.append(list(map(int, input().split())))

result = zigzag_scan(matrix)

print(' '.join(map(str, result)))