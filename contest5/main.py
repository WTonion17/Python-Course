from math import *

# def bai1_chan(a,n):
#     cnt = 0
#     for i in range(n):
#         if a[i] % 2 == 0:
#             cnt += 1
#     print(cnt)

# def bai1_le(a,n):
#     cnt = 0
#     for i in range(n):
#         if a[i] % 2 != 0:
#             cnt += 1
#     print(cnt)        

# def bai1_tongchan(a,n):
#     sum = 0
#     for i in range(n):
#         if a[i] % 2 == 0:
#             sum += a[i]
#     print(sum)
    

# def bai1_tongle(a,n):
#     sum = 0
#     for i in range(n):
#         if a[i] % 2 != 0:
#             sum += a[i]
#     print(sum)

def nt(n):
    if n < 2: return False
    
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    Avg = sum(x for x in a if nt(x)) / sum(1 for x in a if nt(x))
    print("{:.3f}".format(Avg))
