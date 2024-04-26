n = int(input())
nums = list(map(int, input().split()))
event = int(input())

counter = 0
for num in nums:
    if num == event:
        counter += 1

print(counter)
