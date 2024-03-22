turns = []
while True:
    x = int(input())
    if x == 0:
        break
    
    curr = []
    for i in range(x):
        n, m = map(int, input().split())
        curr.append(n)
        curr.append(m)
    turns.append(curr)

for i, v in enumerate(turns):
    aldo, beto = 0, 0
    for j in range(0, len(v), 2):
        aldo += v[j]
        beto += v[j+1]
    print(f'Teste {i+1}')
    if aldo > beto:
        print('Aldo', end='\n\n')
    else:
        print('Beto', end='\n\n')

