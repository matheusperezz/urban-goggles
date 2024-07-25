P = input().replace(' ', '')
occur, s = map(str, input().split(" "))
occur = int(occur)
len_phr = len(P)

total = 0

i = 0
while i < len_phr:
    if P[i] == s[0] and i + len(s) - 1 < len_phr:
        if P[i:i+len(s)] == s:
            total += 1
            i += len(s)
            continue
    
    i += 1
    
        
    

print(total)
if total == occur:
    print('SIM!')
else:
    print('NAO!')