dts = []
while True:
    try:
        line = input()
        if not line:
            break
        day, mon, year = map(int, line.strip().split())
        dts.append((day, mon, year))
    except EOFError:
        break

dts.sort(key=lambda dt: (dt[2], dt[1], dt[0]))
for dt in dts:
    print(f'{dt[0]} {dt[1]} {dt[2]}')