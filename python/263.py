n = int(input())
spc = n-1
for i in range(1, n+1):
    val = ">"*spc + "#"*i
    print(val)
    spc -= 1