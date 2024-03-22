def solve(results):
    best_balance = 0
    best_start = 0
    best_end = 0

    n = len(results)
    for start in range(n):
        balance = 0
        for end in range(start, n):
            balance += results[end]
            if balance > best_balance or (balance == best_balance and end - start > best_end - best_start):
                best_balance = balance
                best_start = start + 1
                best_end = end + 1
    return best_start, best_end if best_balance > 0 else None


matchs = []
while True:
    test = 1
    x = int(input())
    if x == 0:
        break
    
    curr = []
    for i in range(x):
        n, m = map(int, input().split())
        curr.append(n-m)
    matchs.append(curr)

for i, v in enumerate(matchs):
    start, end = solve(v)
    print(f'Teste {i+1}')
    if start is None or end is None:
        print('nenhum')
        print('')
    else:
        print(f'{start} {end}')
        print('')