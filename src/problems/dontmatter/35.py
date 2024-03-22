n = int(input())
is_prime = True
for i in range(2, n//2):
    if n % i == 0:
        is_prime = False

if is_prime:
    print('sim')
else:
    print('nao')