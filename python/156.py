n, m = map(int, input().split())
ships = list(map(int, input().split()))
attacks = list(map(int, input().split()))
destroyed_ships = 0

for a in attacks:
    if ships[a] == 1 and a-1 >= 0 and a+1 < len(ships):
        if ships[a-1] == 1 and ships[a+1] == 1:
            destroyed_ships += 1


print(destroyed_ships)
