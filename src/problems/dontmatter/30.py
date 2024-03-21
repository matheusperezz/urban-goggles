def solve(arr):
    for i, v in enumerate(arr):
        if i+1 == v:
            return i+1

main_list = []
while True:
    i = int(input())
    if i == 0:
        break
    
    l = list(map(int, input().split()))
    main_list.append(l)

for i, m in enumerate(main_list):
    print(f'Teste {i+1}')
    print(solve(m))
    print()
