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

# def bai20(n):
#     if n == 1: return 0
#     res1, res2,res3 = 10**9,10**9,10**9
#     if n % 2 == 0: 
#         res1 = bai20(n // 2) + 1
#     if n % 3 == 0: 
#         res2 = bai20(n // 3) + 1
#     if n > 1: 
#         res3 = bai20(n - 1) + 1
#     return min(res1,res2,res3)

# def bai21(a, left, right):
#     if left >= right:
#         return True
#     else:
#         if a[left] != a[right]:
#             return False
#         else:
#             return bai21(a, left + 1, right - 1)

# def left_print(a, n):
#     if n >= 1:
#         left_print(a, n - 1)
#         print(a[n - 1], end=" ")


# def right_print(a, n):
#     if n >= 1:
#         print(a[n - 1], end=" ")
#         right_print(a, n - 1)

# def bai23(a, n):
#     if n >= 1:
#         if a[n - 1] % 2 != 0:
#             return False
#         return bai23(a, n - 1)
#     else:
#         return True

# def bai24(a,n):
#     if n >= 2:
#         if a[n - 1] <= a[n - 2]: return False
#         return bai24(a,n - 1)
#     else: return True

def binary_search(a,x,n):
    if n >= 1:
        if a[n - 1] == x: return True
        return binary_search(a,x,n-1)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    if binary_search(a,x,n):
        print("1")
    else:
        print("0")


    
    
