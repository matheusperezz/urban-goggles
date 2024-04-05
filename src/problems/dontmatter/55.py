results = []
test = 1
while True:
    participants, rounds = map(int, input().split())
    if participants == rounds == 0:
        break
    
    players_order = list(map(int, input().split()))

    for _ in range(rounds):
        infos = list(map(int, input().split()))
        n_participants = infos[0]
        command = infos[1]
        players_movement = infos[2:]
        players_order = [players_order[i] for i,p in enumerate(players_movement) if p == command]

    print(f'Teste {test}')
    print(players_order[0])                
    print()
    test += 1
    

