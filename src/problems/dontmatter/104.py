name = input().strip()
size = len(name)
if size <= 4:
    print('GRUPO A')
elif 5 <= size <= 10:
    print('GRUPO B')
else:
    print('GRUPO C')