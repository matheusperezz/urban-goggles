time = int(input())
n = int(input())
dmgs = list(map(int, input().split()))

total_dmg = 0
for num in dmgs:
    total_dmg += num * time

if total_dmg < 28000:
    print('O BAD venceu!')
else:
    print('Macacos venceram!')