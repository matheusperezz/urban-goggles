pok = {}
l = 0
while True:
    p = input()
    if p == 'FIM': break
    l += 1
    if p in pok.keys():
        pok[p] += 1
    else:
        pok[p] = 1

ordered_pok = dict(sorted(pok.items()))
for poke, population in ordered_pok.items():
    percent = (population / l) * 100 
    print(f'{poke} {percent:.2f}')