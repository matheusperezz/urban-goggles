peoples = {}
round = 1
while True:
    val = int(input())
    if val == 0: break

    curr_peoples = []
    for _ in range(val):
        name = input()
        values = list(map(int, input().split()))
        values.sort()
        total = sum(values[1:-1])
        p = {
            "name": name,
            "points": total
        }
        curr_peoples.append(p)
    ordered_peoples = sorted(curr_peoples, key=lambda x: (-x['points'], x['name']))
    print(f'Teste {round}')
    last_point = 0
    position = 0
    for i, p in enumerate(ordered_peoples):
        n = p["name"]
        po = p["points"]
        if p['points'] != last_point:
            print(f'{i+1} {po} {n}')
            position = i+1
        else:
            print(f'{position} {po} {n}')
        last_point = po
    print()
    round += 1
