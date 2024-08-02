from math import floor

def split_list(nums):
    sublist = []
    current_sublist = []

    for item in nums:
        if item == 'FIM':
            sublist.append(current_sublist)
            current_sublist = []
        else:
            item = int(item)
            current_sublist.append(item)
    
    if current_sublist:
        sublist.append(current_sublist)
    
    return sublist

nums = []
while True:
    try:
        line = input()
        if not line:
            break
        
        nums.append(line)
    except EOFError:
        break

operations = split_list(nums)[:-1]

for op in operations:
    k = len(op)
    if k > 2:
        n_max = max(op)
        n_min = min(op)
        m = floor((sum(op) - n_max - n_min) / (k - 2))
    elif k == 2:
        m = floor(sum(op) / k)
    else:
        m = op[0]
    
    print(m)
