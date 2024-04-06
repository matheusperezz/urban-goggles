def is_multiple_of_11(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        digit = int(number[i])
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    diff = abs(odd_sum - even_sum)

    return diff == 0 or diff % 11 == 0

while True:
    number = input().strip()
    if number == '0':
        break

    if is_multiple_of_11(number):
        print(number, "is a multiple of 11.")
    else:
        print(number, "is not a multiple of 11.")