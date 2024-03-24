n = int(input())
acc = list(map(int, input().split()))
t = int(input())

if sum(acc) == t:
    print('Acertou')
else:
    print('Errou')