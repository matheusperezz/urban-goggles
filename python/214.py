N = int(input())
nms = []
for _ in range(N):
    n = input()
    nms.append(n)

nms.sort()
for n in nms:
    print(n)