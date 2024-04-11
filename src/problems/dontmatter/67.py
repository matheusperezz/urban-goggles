test = 1
while True:
    val = int(input())
    if val == 0:
        break
    p1 = input()
    p2 = input()
    print(f'Teste {test}')
    for _ in range(val):
        n1, n2 = map(int, input().split())
        if (n1+n2) % 2 == 0:
            print(p1)
        else:
            print(p2)
    test += 1