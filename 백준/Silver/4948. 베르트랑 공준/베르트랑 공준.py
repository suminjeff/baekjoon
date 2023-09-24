import sys
input = sys.stdin.readline



num = 123457*2
primes = [0] * (num+1)
for i in range(num):
    primes[i] = i

for i in range(2, num+1):
    if primes[i] == 0:
        continue
    for j in range(i+i, num+1, i):
        primes[j] = 0


while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if primes[i] != 0:
            cnt += 1
    print(cnt)