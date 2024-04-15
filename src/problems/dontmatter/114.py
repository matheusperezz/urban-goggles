n = int(input())
d = {}
for i in range(n):
    na, v = input().split()
    v = int(v)
    d[na] = v

k = int(input())
books = list(input().split(" "))

for b in books:
    if b in d:
        val = d[b]

        if val == 1:
            print("Disponivel")
        elif val == 2:
            print("Emprestado")
    else:
        print("Nao encontrado")
