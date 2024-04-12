test = 1
while True:
    n = int(input())
    if n == 0:
        break
    x_assis = []
    y_assis = []
    for _ in range(n):
        x, y = map(int, input().split())
        x_assis.append(x)
        y_assis.append(y)

    x_assis.sort()
    y_assis.sort()
    print(f'Teste {test}')
    print(f'{x_assis[n//2]} {y_assis[n//2]}')
    print()
    test += 1