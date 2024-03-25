nums = []
while True:
    n, p = map(int, input().split())
    if n == p == 0:
        break
    integer_pages = n // p
    rest_of_division = n % p
    if rest_of_division > 0:
        integer_pages += 1
    nums.append(integer_pages)

for n in nums:
    if n <= 6:
        print('Poodle')
    elif n < 20:
        v = n-6
        print('Poo' + 'o'*v + 'dle')
    else:
        print('Poooooooooooooooodle')