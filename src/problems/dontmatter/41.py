def dentro_do_tabuleiro(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def eh_buraco(x, y, buracos):
    return (x, y) in buracos

def contar_movimentos(N, movimentos, buracos):
    x, y = 4, 4
    movimentos_feitos = 0

    for movimento in movimentos:
        if movimento == 1:
            novo_x, novo_y = x + 1, y - 2
        elif movimento == 2:
            novo_x, novo_y = x + 2, y - 1
        elif movimento == 3:
            novo_x, novo_y = x + 2, y + 1
        elif movimento == 4:
            novo_x, novo_y = x + 1, y + 2
        elif movimento == 5:
            novo_x, novo_y = x - 1, y + 2
        elif movimento == 6:
            novo_x, novo_y = x - 2, y + 1
        elif movimento == 7:
            novo_x, novo_y = x - 2, y - 1
        elif movimento == 8:
            novo_x, novo_y = x - 1, y - 2

        if dentro_do_tabuleiro(novo_x, novo_y):
            x, y = novo_x, novo_y
            if eh_buraco(x, y, buracos):
                movimentos_feitos += 1
                break
            else:
                movimentos_feitos += 1
        else:
            movimentos_feitos += 1
            break

    return movimentos_feitos

N = int(input())
movimentos = list(map(int, input().split()))

buracos = [(2, 2), (5, 3), (1, 4), (2, 4)]

resultado = contar_movimentos(N, movimentos, buracos)

print(resultado)