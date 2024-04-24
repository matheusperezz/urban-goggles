nums = []
for _ in range(4):
    nums.append(float(input()))

result = sum(nums)/4

if result >= 5.0:
    print('Parabens bruxao, eh nois que voa, voce passou!')
else:
    print('Voce nao passou, tente usar a varinha na proxima vez!')
