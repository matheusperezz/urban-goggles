n = int(input())
words = []
for _ in range(n):
    val = input()
    words.append(val)

words.sort()
for w in words:
    print(w)
