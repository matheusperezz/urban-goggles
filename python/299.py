n = int(input())
frames = []
for _ in range(n):
    operation, level = input().split(" ")
    level = int(level)
    frames.append((operation, level))
    
personagem_nivel = 1

for operacao, valor in frames:
    if operacao == 't':
        personagem_nivel += valor
        if personagem_nivel >= 5:
            print("Aventura concluida")
            break
    elif operacao == 'm':
        print("Combate iniciado")
        if personagem_nivel >= valor:
            print("VITORIA")
            personagem_nivel += 1
            if personagem_nivel >= 5:
                print("Aventura concluida")
                break
        else:
            print("Derrota! Fim da aventura")
            break
    elif operacao == 'b':
        personagem_nivel = max(0, personagem_nivel - valor)