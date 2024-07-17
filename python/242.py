N = int(input())
nums = list(map(int, input().strip().split()))
V, T = map(int, input().strip().split())
T_V = nums[T]
Vs = sum(nums)

if Vs > V:
    print('Estamos classificados!')
elif Vs < V:
    print('Nao foi dessa vez...')
else:
    if T_V == 1:
        print('Vamos jogar o desempate.')
    elif T_V == 2:
        print('Estamos classificados!')
    else:
        print('Nao foi dessa vez...')

