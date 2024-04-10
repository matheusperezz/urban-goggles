t = int(input())
will_explode = False
while True:
    val = int(input())
    if val == 0:
        break
    if val > t:
        will_explode = True

if will_explode:
    print('ALARME')
else:
    print('O Havai pode dormir tranquilo')