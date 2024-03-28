n = int(input())
nums = [int(x) for x in input().split()]

occurs = {}
for n in nums:
    if n in occurs:
        occurs[n] += 1
    else:
        occurs[n] = 1

bigger_qnt = 0

for _, v in occurs.items():
    if v > bigger_qnt:
        bigger_qnt = v

best_nums = []
for key, value in occurs.items():
    if value == bigger_qnt:
        best_nums.append(key)

print(max(best_nums))
