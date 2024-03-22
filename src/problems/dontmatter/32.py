number_reading, max_capacity = map(int, input().split())
readings = []
for _ in range(number_reading):
    x, y = map(int, input().split())
    readings.append(x)
    readings.append(y)

curr = 0
is_full = False
for i in range(0, len(readings), 2):
    if curr - readings[i] < 0:
        curr = 0
    else:
        curr -= readings[i]
    curr += readings[i+1]
    if curr > max_capacity:
        is_full = True
        break

if is_full:
    print('S')
else:
    print('N')
    
