n = int(input())
d = {}
for i in range(n):
    key, word = input().split()
    d[key] = word

m = int(input())
phrase = input().split(" ")
for j in range(m):
    if phrase[j] in d.keys():
        phrase[j] = d[phrase[j]]
    
for word in phrase:
    print(word, end=' ')
print()