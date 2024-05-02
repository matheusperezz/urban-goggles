max_exp = int(input())
n = int(input())
exp = list(map(int, input().split()))
bonus = list(map(int, input().split()))

points = 0
for i in range(n):
    points += exp[i] * bonus[i]

if points >= max_exp:
    print('Upou de Nivel!')
else:
    print('Nao foi dessa vez!')