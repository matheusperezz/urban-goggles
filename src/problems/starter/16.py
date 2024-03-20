cv, ce, cs, fv, fe, fs = map(int, input().split())
c_points = (cv * 3) + ce
f_points = (fv * 3) + fe

if c_points > f_points:
    print('C')
elif f_points > c_points:
    print('F')
else:
    if cs > fs:
        print('C')
    elif fs > cs:
        print('F')
    else:
        print('=')