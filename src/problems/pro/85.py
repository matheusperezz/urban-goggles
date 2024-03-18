def isIllegal(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1

        else:
            return "sim"
    return "nao"

n = int(input())
illegal_numbers = list(map(int, input().split()))
nums = []
try:
    while True:
        x = input()
        if x == '':
            break
        else:
            nums.append(int(x))
except EOFError:
    pass

illegal_numbers.sort()
for n in nums:
    print(isIllegal(illegal_numbers, n))