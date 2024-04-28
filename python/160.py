def found_dupl(nums):
    copy = []
    for num in nums:
        if num in copy:
            return num
        else:
            copy.append(num)

    return -1


n = int(input())
nums = list(map(int, input().split()))
result = found_dupl(nums)

print(result)
