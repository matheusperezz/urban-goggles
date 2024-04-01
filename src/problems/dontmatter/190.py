n = int(input())
geleia, tradicional = 0, 0
for _ in range(n):
    x = int(input())
    if x == 11:
        geleia += 1
    else:
        tradicional += 1

if geleia >= tradicional:
    print('Geleia')
else:
    print('Tradicional')