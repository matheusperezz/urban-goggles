class Aluno:
    def __init__(self, codigo, media):
        self.codigo = codigo
        self.media = media

while True:
    n = int(input())
    if n == 0:
        break
    
    alunos = []
    
    for _ in range(n):
        codigo, media = map(int, input().split())
        alunos.append(Aluno(codigo, media))
    
    melhor_media = max(aluno.media for aluno in alunos)

    print(f"Turma {n}")
    for aluno in alunos:
        if aluno.media == melhor_media:
            print(aluno.codigo, end=" ")
    print("\n")
