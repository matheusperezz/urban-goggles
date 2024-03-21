cards = list(map(int, input().split()))
sorted_cards = sorted(cards)
reversed_cards = sorted(cards, reverse=True)
if cards == sorted_cards:
    print('C')
elif cards == reversed_cards:
    print('D')
else:
    print('N')