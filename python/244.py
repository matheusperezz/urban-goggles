n, t = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = len(nums)-1
nums.sort()
while left != right:
    if nums[left]+nums[right] == t:
        break
    elif nums[left]+nums[right] > t:
        right -= 1
    else:
        left += 1
        

print(f'{nums[left]} {nums[right]}')
