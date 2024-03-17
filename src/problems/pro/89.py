def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def degree_nine(n):
    if n == 9:
        return 1
    count = 0
    while n > 9:
        n = digit_sum(n)
        count += 1
    return count if n == 9 else None

list = []
while True:
    n = int(input())
    if n == 0:
        break
    list.append(n)

for d in list:
    degree = degree_nine(d)
    if degree is None:
        print(f'{d} is not a multiple of 9.')
    else:
        print(f'{d} is a multiple of 9 and has 9-degree {degree_nine(d)}.')