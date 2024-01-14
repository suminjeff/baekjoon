import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
DP = [P[i] for i in range(N+1)]
DP[1] = P[1]
for i in range(2, N+1):
    for j in range(1, i+1):
        DP[i] = min(DP[i], P[j] + DP[i-j])
print(DP[N])