import sys
input = sys.stdin.readline
import math

def isprime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    while not isprime(n):
        n += 1
    print(n)