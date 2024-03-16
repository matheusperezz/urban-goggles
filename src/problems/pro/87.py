cache = {}

def hanoi(n, orig, dest, temp):
    if n == 1:
        return 1
    if (n, orig, dest, temp) in cache:
        return cache[(n, orig, dest, temp)]
    steps = 0
    steps += hanoi(n-1, orig, temp, dest)
    steps += 1
    steps += hanoi(n-1, temp, dest, orig)
    cache[(n, orig, dest, temp)] = steps
    return steps

list = []
while True:
    n = int(input())
    if n == 0:
        break
    list.append(n)

for i, v in enumerate(list):
    total_steps = hanoi(v, 'a', 'b', 'c')
    print(f'Teste {i+1}')
    print(total_steps)
    print()
