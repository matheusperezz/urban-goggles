"""
Entrada	Saída
6
EDUCOMIDIAS
AMAR
AACA
QUALIFICA
GREEN
FALCON
  
Equipe 1:
EDUCOMIDIAS
AMAR
QUALIFICA
GREEN
FALCON
Equipe 2:
AACA
"""

def get_ascii_sum_is_even(word):
    c = 0
    for char in word:
        c += ord(char)
    return c % 2 == 0

first_team, second_team = [], []
projects = []
n = int(input())
for i in range(n):
    p = input()
    if get_ascii_sum_is_even(p):
        second_team.append(p)
    else:
        first_team.append(p)

if first_team:
    print('Equipe 1:')
    for p in first_team:
        print(p)
else:
    print('Equipe 1 responsavel por todos os incidentes de TI')

if second_team:
    print('Equipe 2:')
    for p in second_team:
        print(p)
else:
    print('Equipe 2 responsavel por todos os incidentes de TI')