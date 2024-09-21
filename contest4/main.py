from math import *

def bintodec(n):
    if n == 0: return 0
    else: bintodec(n // 2)
    print(n % 2,end= '')

if __name__ == '__main__':
    n = int(input())
    bintodec(n)
