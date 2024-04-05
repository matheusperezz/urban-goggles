def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

input_list = []
while True:
    try:
        num = int(input())
        input_list.append(num)
    except:
        break

print(list_length(input_list))
