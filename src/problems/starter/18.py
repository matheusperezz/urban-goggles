# 30 100 60 50
p1, c1, p2, c2 = map(int, input().split())
left = p1 * c1
right = p2 * c2

if left > right:
    print('-1')
elif right > left:
    print('1')
else:
    print('0')
