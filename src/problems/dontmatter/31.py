main_list = []
while True:
    i = int(input())
    if i == 0:
        break
    curr = []
    for _ in range(i):
        x , y = map(int, input().split())
        curr.append(x)
        curr.append(y)

    main_list.append(curr)

for i, m in enumerate(main_list):
    print(f'Teste {i+1}')
    diff = 0
    for j in range(0, len(m), 2):
        diff += m[j] - m[j+1]
        print(diff)
    print()