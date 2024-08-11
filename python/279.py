pots = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4, 32: 5, 64: 6, 128: 7, 256: 8, 512: 9}
max_two_pot = -1

N = int(input())
for _ in range(N):
    val = int(input())
    if val in pots.keys:
        max_two_pot = val

if max_two_pot > -1:
    print(pots[max_two_pot])
else:
    print(0)