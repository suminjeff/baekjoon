import sys
input = sys.stdin.readline


primes = [False, False] + [True] * 999999

for i in range(2, 1000001):
    if primes[i]:
        for j in range(i*2, 1000001, i):
            primes[j] = False
T = int(input())
for i in range(1, T+1):
    cnt = 0
    N = int(input())
    for j in range(2, N//2 + 1):
        if primes[j] and primes[N-j]:
            cnt += 1
    print(cnt)