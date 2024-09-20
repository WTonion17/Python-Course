from math import *

a,b,c,d = map(float,input().split())

S = (a+b+c*2+d*3) / 7

print(S)

if S >= 8:
    print('GIOI')
elif S >=6.5 and S < 8:
    print('KHA')
elif S >=5:
    print('TRUNG BINH')
else: print('YEU')


