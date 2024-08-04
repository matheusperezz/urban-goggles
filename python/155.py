lines = []
N = 0
while True:
    try:
        line = input()
        if line == '0 #':
            break
        lines.append(line)
        N += 1
    except EOFError:
        break

output = ["" for _ in range(N)]
for l in lines:
    idx, name = l.strip().split()
    idx = int(idx)
    output[idx-1] = name

for o in output:
    print(o)
