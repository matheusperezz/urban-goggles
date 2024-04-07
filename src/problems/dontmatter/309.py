pistas, pessoas_por_pista, alunos = map(int, input().split())
if alunos < pistas*pessoas_por_pista:
    print('S')
else:
    print('N')
