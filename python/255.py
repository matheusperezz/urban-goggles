def count_friends(friends, cls):
    count = 0
    for c in cls:
        if c in friends:
            count += 1
    return count

n = int(input())
friends = list(map(int, input().strip().split()))

m = int(input())
for _ in range(m):
    k = int(input())
    cls = list(map(int, input().strip().split()))
    qnt = count_friends(friends, cls)
    if qnt == len(friends):
        print('Todos reunidos!')
    else:
        print(qnt)