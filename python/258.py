warriors = []
j, k = map(int, input().split())
for i in range(j):
    name, power = input().split()
    power = int(power)
    warriors.append({'name': name, 'power': power})

warriors.sort(key=lambda x: x['power'], reverse=True)
for i in range(k):
    if i == len(warriors):
        break
    warrName = warriors[i]['name']
    warrPower = warriors[i]['power']
    print(f'{warrName} {warrPower}')
