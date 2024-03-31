peixes = int(input())
valor_por_unidade = int(input())
total = peixes * valor_por_unidade

if total < 500:
    print('Paciência Firmino!')
elif total < 1800:
    print('Vara de Bambu')
elif total < 7500:
    print('Vara de Fibra de Vidro')
else:
    print('Vara de Iridio')