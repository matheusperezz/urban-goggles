money = []
while True:
    x = int(input())
    if x == 0:
        break
    money.append(x)

for i, m in enumerate(money):
    output = [0, 0, 0, 0]
    output[0] = m // 50
    m = m % 50
    output[1] = m // 10
    m = m % 10
    output[2] = m // 5
    m = m % 5
    output[3] = m // 1
    print(f'Teste {i+1}')
    for o in output:
        print(o, end=' ')
    print('\n')
