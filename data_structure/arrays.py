def binary_search(arr, target):
    left, right = 0, len(arr)-1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]
        if mid_element > target:
            right = mid - 1
        elif mid_element < target:
            left = mid + 1
        else:
            return mid
    return -1

arr = [1,3,5,7,9,11,99,1298]
target = 5
output = binary_search(arr, target)
print(output)                                               