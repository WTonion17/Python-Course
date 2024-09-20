from math import *
# tinh tong uoc va dem uoc cua 1 so nguyen
# def demuoc(n):
#     cnt = 0
#     for i in range(1,isqrt(n) + 1):
#         if n % i == 0:
#             cnt += 1
#             if i != n // i:
#                 cnt += 1
#     return cnt

# def tonguoc(n):
#     tong = 0
#     for i in range(1, isqrt(n) + 1):
#         if n % i == 0:
#             tong += i
#             if i!= n // i:
#                 tong += n // i
#     return tong

# kiemtra so nguyen to
# def prime(n):
#     if n < 2: return False
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             return False
#     return True 

#phan tich thua so nguyen to
# def pt(n):
#     for i in range(2, isqrt(n) + 1):
#         if n % i == 0:
#             while n % i == 0:
#                 print(i,end = ' ')
#                 n //= i
#     if n > 1:
#         print(n)

# kiem tra so chinh phuong
# def square(n):
#     can = isqrt(n)
#     return can * can == n
#kiemtra so lap phuong
# def cube(n):
#     can = int(pow(n,1/3))
#     return can ** 3 == n or ((can + 1) ** 3 == n) 

#uoc chung lon nhat
# def gcd(a,b):
#     while b != 0:
#         a,b = b, a % b
#     return a
#boi chung nho nhat
# def lcm(a,b):
#     return a * b / gcd(a,b)

# kiem tra so thuan nghich8
# def palin(n):
#     rev = 0
#     temp = n
#     while n != 0:
#         rev = rev * 10 + n % 10
#         n // 10
#     return rev == temp

if __name__ == '__main__':
    n = int(input())
    # print(demuoc(n))
    # print(tonguoc(n))
    # if prime(n):
    #     print('YES')
    # else: print('NO')
    # pt(n)