x, y = map(int, input().split())
if x < 1:
    print('branca')
else:
    if y < 72:
        print('amarela')
    elif y < 90:
        print('roxa')
    elif y < 110:
        print('verde')
    elif y < 120:
        print('azul')
    else:
        print('marrom')
