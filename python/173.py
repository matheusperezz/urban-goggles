from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

while True:
    val = int(input())
    if val == 0: break
    
    if is_prime(val):
        print('O numero de cadeiras eh primo!')
    else:
        print('O numero de cadeiras nao eh primo!')
