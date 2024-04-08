n = int(input())
most_powerful = 0
for _ in range(n):
    power = int(input())
    if power > most_powerful:
        most_powerful = power

print(most_powerful)