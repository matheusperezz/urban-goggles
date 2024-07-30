s1 = input()
s2 = input()

m1 = {}
m2 = {}

for s in s1:
    if s in m1.keys():
        m1[s] += 1
    else:
        m1[s] = 1
    
for s in s2:
    if s in m2.keys():
        m2[s] += 1
    else:
        m2[s] = 1

if m1 == m2:
    print('Sim')
else:
    print('Nao')