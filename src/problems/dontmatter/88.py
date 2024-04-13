def f91(n):
    if n <= 100:
        return f91(f91(n+11))
    else:
        return n - 10

while True:
    val = int(input())
    if val == 0:
        break
    r = f91(val)
    print(f'f91({val}) = {r}')
