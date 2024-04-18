def ponto_divisao(N, comprimentos):
    soma_total = sum(comprimentos)

    soma_esquerda = 0
    
    for i in range(N):
        soma_esquerda += comprimentos[i]
        
        if soma_esquerda == soma_total - soma_esquerda:
            return i + 1
            
N = int(input())
comprimentos = list(map(int, input().split()))
ponto = ponto_divisao(N, comprimentos)
print(ponto)

