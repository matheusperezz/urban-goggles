is_infectada, dias_infectada = input().split()
dias_infectada = int(dias_infectada)

if is_infectada == 'N':
    print('Acesso permitido!')
else:
    if dias_infectada < 7:
        print('Acesso negado! Isolamento urgente')
    elif dias_infectada < 30:
        print('Acesso negado! Fique em observacao')
    else:
        print('Imune! Siga para um local seguro')