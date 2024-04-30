def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def total_necessary(values, m):
    total = 0
    for val in values:
        total += m // gcd(m, val)
    return total

def calc(n, m, b, vals):
    total_withoutb = total_necessary(vals, m)
    total_withb = total_necessary(vals + [b], m)
    return total_withb, total_withoutb

n, m, b = map(int, input().split())
vals = list(map(int, input().split()))

withB, withoutB = calc(n, m, b, vals)
if withB == withoutB:
    print('indiferente')
else:
    print(abs(withoutB - withB))
