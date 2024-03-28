def is_kaprekar(n):
    if n == 1:
        return True

    sq = n * n
    sq_str = str(sq)

    for i in range(1, len(sq_str)):
        p1 = int(sq_str[:i])
        p2 = int(sq_str[i:])

        if p2 > 0 and p1 + p2 == n:
            return True
    
    return False

nums = []
while True:
    x = int(input())
    if x == 0:
        break
    nums.append(x)

for n in nums:
    if is_kaprekar(n):
        print(f'{n}: S')
    else:
        print(f'{n}: N')