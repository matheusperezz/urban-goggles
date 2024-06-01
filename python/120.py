"""
3
maria andrade ferreira
felipe barros silva matos
joao barbosa
  
M. A. Ferreira
F. B. S. Matos
J. Barbosa
"""
n = int(input())
for i in range(n):
    line = input().split(" ")
    m = len(line)
    for j in range(m):
        if j != m-1:
            print(f'{line[j][0].upper()}.', end=' ')
        else:
           s = line[j]
           s = s[0].upper() + s[1:]
           print(s)
