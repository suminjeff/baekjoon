import sys
input = sys.stdin.readline

# 유클리드 호제법

def gcd(m, n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)


n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())
n = n1*d2 + n2*d1
d = d1*d2

cd = gcd(n, d)
print(n//cd, d//cd)