matchs = int(input())
ak, ad = [], []
bk, bd = [], []
for _ in range(matchs):
    k, d = map(int, input().split())
    ak.append(k)
    ad.append(d)

for _ in range(matchs):
    k, d = map(int, input().split())
    bk.append(k)
    bd.append(d)

a_kd = 0
b_kd = 0
sumkills = 0
sumdeaths = 0

for i in range(matchs):
    sumkills += ak[i]
    sumdeaths += ad[i]

a_kd = sumkills / sumdeaths

sumkills = 0
sumdeaths = 0

for i in range(matchs):
    sumkills += bk[i]
    sumdeaths += bd[i]

b_kd = sumkills / sumdeaths

if a_kd > b_kd:
    print("Parabens Alberto!")
    print("{:.2f}".format(a_kd))
elif b_kd > a_kd:
    print("Parabens Bruno!")
    print("{:.2f}".format(b_kd))
else:
    print("Empate")
