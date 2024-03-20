def maior_soma_areas(L, N):
    soma_areas = 0
    tamanho = 1
    while N > 0 and tamanho <= L:
        quantidade = min(N, L // tamanho)
        soma_areas += tamanho ** 2 * quantidade
        N -= quantidade
        tamanho += 1
    return soma_areas

# Entrada
L, N = map(int, input().split())

# Saída
print(maior_soma_areas(L, N))