n = int(input())
total_weight = 0
for _ in range(n):
    name, weight = input().split(" ")
    total_weight += int(weight)

max_weight = int(input())

if total_weight > max_weight:
    print('Vamos virar almoço de aranhas gigantes!')
else:
    print('Vamos todos encontrar a montanha!')