is_winner = False
while True:
    line = input().replace(" ", "")
    if line == "FIMFIMFIM": break
    if line == "NAOSIMNAO":
        is_winner = True

if is_winner:
    print('VITORIA')
else:
    print('DERROTA')
