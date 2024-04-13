n = int(input())
if n < 16:
    print('não pode votar nem ser presa')
elif n < 18:
    print('pode votar')
else:
    print('pode votar e ser presa')