"""
Entre 0% a 50%
“Seu pokemon nao fara progresso em batalhas”
  
Entre 51% a 66%
  
“Seu pokemon esta acima da media”
Entre 67% a 79%
“Seu pokemon certamente me chamou atencao”
  
Entre 80% a 100%
“Seu pokemon e uma maravilha”
"""
a, d, p = map(int, input().split())
result = int(((a+d+p)/110)*100)

if result in range(0, 51):
    print('Seu pokemon nao fara progresso em batalhas')
elif result < 66:
    print('Seu pokemon esta acima da media')
elif result < 80:
    print('Seu pokemon certamente me chamou atencao')
elif result < 100:
    print('Seu pokemon e uma maravilha')
else:
    print('Hum, parece que houve um erro')