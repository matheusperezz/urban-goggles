def solve(X, Y, L1, H1, L2, H2):
    options = [
        (L1 + L2 <= X and max(H1, H2) <= Y),
        (max(L1, L2) <= X and H1 + H2 <= Y),
        (H1 + H2 <= X and max(L1, L2) <= Y),
        (max(H1, H2) <= X and L1 + L2 <= Y),
        (H1 + L2 <= X and max(L1, H2) <= Y),
        (L1 + H2 <= X and max(H1, L2) <= Y)
    ]
    return any(options)
    

x, y = map(int, input().split())
l1, h1 = map(int, input().split())
l2, h2 = map(int, input().split())

if solve(x, y, l1, h1, l2, h2):
    print('S')
else:
    print('N')