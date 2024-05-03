def count_cons(word):
    counter = 0
    vogals = ['a', 'e', 'i', 'o', 'u']
    for w in word:
        if w not in vogals and w != " ":
            counter += 1
    return counter

n, m = map(int, input().split())
for _ in range(n):
    val = input()
    if count_cons(val) > m:
        print(0)
    else:
        print(1)