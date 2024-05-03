def printarr(arr):
    for n in arr:
        print(n, end=' ')
    print()

def m():
    n = int(input())
    m = int(input())
    total = [x for x in range(1, n+1)]
    if m == 0:
        printarr(total)
        return
    nums = list(map(int, input().split()))

    for num in total:
        if num not in nums:
            print(num, end=' ')
    print()

m()