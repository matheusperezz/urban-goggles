ondas, clones_naruto = map(int, input().split())
defendeu_vila = True
for _ in range(ondas):
    zetsus, clones = map(int, input().split())
    clones_naruto += clones
    if zetsus > clones_naruto:
        defendeu_vila = False
    clones_naruto -= zetsus   

if defendeu_vila:
  print('Naruto defendeu a Vila')
else:
  print('Madara venceu')
