from math import *

# def bai14(n):
#     cnt = 0 
#     if n < 10: return 1
#     return 1 + bai14(n // 10)

# def bai15(n):
#     if n < 10: return n
#     return bai15(n // 10)

# def bai16_maxdigit(n):
#     if n < 10: return n
#     return max(n % 10, bai16_maxdigit(n // 10))

# def bai16_mindigit(n):
#     if n < 10: return n
#     return min(n % 10, bai16_mindigit(n // 10))

def bai17_left(n):
    if n < 10: print(n, end = ' ')
    else: 
        bai17_left(n // 10) 
        print(n % 10,end = ' ')


def bai17_right(n):
    if n < 10: print(n, end= ' ')
    else: 
        print(n % 10,end = ' ')
        bai17_left(n // 10) 

if __name__ == '__main__':
    n = int(input())
    bai17_left(n)
    print()
    bai17_right(n)
