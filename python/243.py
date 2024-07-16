Q = int(input())
jun_figs = list(map(int, input().strip().split()))
qnt_jun_figs = list(map(int, input().strip().split()))
N = int(input())
figs = list(map(int, input().strip().split()))

d = {}
for i in range(Q):
    d[jun_figs[i]] = qnt_jun_figs[i]

for fig in figs:
    if fig not in jun_figs:
        print('Quero')
    else:
        if d[fig] == 1:
            print('Apenas uma')
        else:
            print('Trocar')
