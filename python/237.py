db = {}
n = int(input())
for i in range(n):
    id, phone, name = input().split(" ")
    db[id] = (phone, name)

m = int(input())
for j in range(m):
    c = input()
    if c in db:
        p = db[c]
        print(f'{p[1]}: {p[0]}')
    else:
        print('Aluno nao encontrado')

print(db)
