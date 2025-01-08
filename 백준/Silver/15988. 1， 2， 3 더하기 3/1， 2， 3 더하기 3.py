import sys

if __name__ == '__main__':
    T = int(input())
    MOD = 1_000_000_009
    MAX_N = 1_000_000
    CACHE = [0]*(MAX_N+1)
    CACHE[0] = CACHE[1] = 1
    CACHE[2], CACHE[3] = 2, 4
    for n in range(4, MAX_N+1):
        CACHE[n] = (CACHE[n-1] + CACHE[n-2] + CACHE[n-3]) % MOD

    for TC in range(T):
        N = int(input())
        print(CACHE[N])