n = int(input())
nums = list(map(int, input().split()))
even, odd = 0, 0
for i in range(n):
    if i % 2 == 0:
        even += nums[i]
    else:
        odd += nums[i]

if even > odd:
    print('Vou ajudar')
else:
    print('Modo Hard')