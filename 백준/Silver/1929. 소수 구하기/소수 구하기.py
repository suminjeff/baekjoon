import sys
input = sys.stdin.readline

from math import sqrt

def isprime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


M, N = map(int, input().split())
for i in range(M, N+1):
    if isprime(i):
        print(i)