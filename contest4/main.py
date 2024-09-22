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

# def bai17_left(n):
#     if n < 10: print(n, end = ' ')
#     else: 
#         bai17_left(n // 10) 
#         print(n % 10,end = ' ')


# def bai17_right(n):
#     if n < 10: print(n, end= ' ')
#     else: 
#         print(n % 10,end = ' ')
#         bai17_left(n // 10) 

# def bai18_tongchan(n):
#     if n < 10:
#         if n % 2 == 0: return n
#         else: return 0
#     if n % 2 == 0:
#         return n % 10 + bai18_tongchan(n // 10)
#     else: return bai18_tongchan(n // 10)

# def bai18_tongle(n):
#     if n < 10:
#         if n % 2 == 0: return 0
#         else: return n
#     if n % 2 == 0:
#         return bai18_tongle(n // 10)
#     else: return n % 10 + bai18_tongle(n // 10)

# def bai19_KTsochan(n):
#     if n < 10:
#         if n % 2 == 0:
#             return 1
#         else: return 0 
#     if n % 2 == 0 and bai19_KTsochan(n // 10) :
#         return 1  
#     else: return 0\

def bai20(n):
    if n == 1: return 0
    res1, res2,res3 = 10**9,10**9,10**9
    if n % 2 == 0: 
        res1 = bai20(n // 2) + 1
    if n % 3 == 0: 
        res2 = bai20(n // 3) + 1
    if n > 1: 
        res3 = bai20(n - 1) + 1
    return min(res1,res2,res3)

if __name__ == '__main__':
    n = int(input())
    print(bai20(n))
