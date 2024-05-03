n = int(input())
nums = []
for _ in range(n):
    val = int(input())
    nums.append(val)

g = (sum(nums)/len(nums)) * 100
if g < 30:
    print('Regiao segura')
elif g <= 50:
    print('Regiao em estado de alerta')
else:
    print('Regiao com alto indice de perda de biodiversidade')