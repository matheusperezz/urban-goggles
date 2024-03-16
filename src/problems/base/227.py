n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

row_start_harry, column_start_ron = map(int, input().split())
harry_points, ron_points = 0, 0

for i in range(n):
    ron_points += matrix[i][column_start_ron]
    matrix[i][column_start_ron] = 0
    harry_points += matrix[row_start_harry][i]        
    matrix[row_start_harry][i] = 0

print(f'Harry {harry_points}')
print(f'Ron {ron_points}')