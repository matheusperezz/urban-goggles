output = []
while True:
    a, v = map(int, input().split())
    if a == v == 0:
        break
    occur = [0 for _ in range(a)]
    for i in range(v):
        x, y = map(int, input().split())
        occur[x-1] += 1
        occur[y-1] += 1
    max_value = max(occur)
    max_idx = [i+1 for i, x in enumerate(occur) if x == max_value]
    output.append(max_idx)

test = 1
for o in output:
    print(f'Teste {test}')
    for p in o:
        print(p, end=' ')
    test += 1
    print('\n')