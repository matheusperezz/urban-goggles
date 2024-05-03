n = int(input())
mlt = 1
spc = n-1
for i in range(1,n+1):
    val = " "*spc + str(i)*mlt
    mlt += 2
    spc -= 1
    print(val)