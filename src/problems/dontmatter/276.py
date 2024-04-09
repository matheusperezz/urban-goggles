"""
Tipos de quarto:

Casal: 2 pessoas
Triplo: 3 pessoas
Quadruplo: 4 pessoas
Familia: 5 pessoas
Saída
A saída consiste em imprimir a frase “Pode reservar! Esses quartos cabem todos.”,
caso a quantidade de quartos seja suficiente para todos, 
ou “Procure outra pousada.”, caso contrário.
"""
mapa_hashe = {
    "Casal": 2,
    "Triplo": 3,
    "Quadruplo": 4,
    "Familia": 5
}

peoples = int(input())
rooms = 0
while True:
    val = input()
    if val == 'FIM':
        break
    rooms += mapa_hashe[val]

if peoples > rooms:
    print('Procure outra pousada.')
else:
    print('Pode reservar! Esses quartos cabem todos.')