x, y = map(int, input().split())
if x in range(1,100) and y in range(1, 100):
    if x > 70 or y > 70:
        print('Coordenada valida e o navio esta longe')
    else:
        print('Coordenada valida e o navio esta perto')
else:
    print('Coordenada invalida')