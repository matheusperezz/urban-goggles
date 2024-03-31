def calcular_posicoes_possiveis(N, M, sapos):
    posicoes = [0] * N 
    
    for sapo in sapos:
        posicao_inicial, pulo = sapo
        posicoes_possiveis = posicao_inicial
        
        while posicoes_possiveis <= N:
            posicoes[posicoes_possiveis - 1] = 1
            posicoes_possiveis += pulo
        
    return posicoes

N, M = map(int, input().split())
sapos = [tuple(map(int, input().split())) for _ in range(M)]

posicoes_possiveis = calcular_posicoes_possiveis(N, M, sapos)

for posicao in posicoes_possiveis:
    print(posicao)
