items = []
while True:
    val = input()
    if val == 'fim': break
    items.append(val)

query = input()
if query in items:
    print('item encontrado')
else:
    print('voce ainda nao descobriu este item')