def is_valid_sudoku(board):
    rows = [[False] * 9 for _ in range(9)]
    columns = [[False] * 9 for _ in range(9)]
    boxes = [[False] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = int(board[i][j]) - 1
            k = (i // 3) * 3 + j // 3
            if rows[i][num] or columns[j][num] or boxes[k][num]:
                return False
            rows[i][num] = True
            columns[j][num] = True
            boxes[k][num] = True
                
    return True

n = int(input())
for i in range(n):
    board = []
    for j in range(9):
        board.append(list(map(int, input().split())))
    print(f'Instancia {i+1}')
    if is_valid_sudoku(board):
        print('SIM')
    else:
        print('NAO')
    print()
            