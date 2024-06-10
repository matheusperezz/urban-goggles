n = int(input())
values = list(map(int, input().split()))
damages = list(map(int, input().split()))
money = int(input())

can_buy = []
# All weapons that i can buy
for i in range(n):
    if values[i] <= money:
        can_buy.append({ 
            "value":values[i],
            "damage":damages[i]
         })

# Best weapon
ordered_weapons = sorted(can_buy, key=lambda x: x["damage"], reverse=True)
if ordered_weapons:
    print(f'{ordered_weapons[0]["value"]} {ordered_weapons[0]["damage"]}')
else:
    print('Yan Pobre')
