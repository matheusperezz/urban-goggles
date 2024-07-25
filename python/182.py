def b_seach(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

N = int(input())
visited = list(map(int, input().strip().split()))
verifieds = list(map(int, input().strip().split()))[:-1]

for v in verifieds:
    r = b_seach(visited, v)
    if r == -1:
        print('Nao foi visitado ainda.')
    else:
        print(r)
