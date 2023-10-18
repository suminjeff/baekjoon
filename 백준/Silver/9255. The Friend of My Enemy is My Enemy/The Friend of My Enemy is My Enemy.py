import sys
input = sys.stdin.readline


K = int(input())
for k in range(1, K+1):
    N, M = map(int, input().split())
    adj_l = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        if s != e:
            if e not in adj_l[s]:
                adj_l[s].append(e)
            if s not in adj_l[e]:
                adj_l[e].append(s)
    S = int(input())
    print(f"Data Set {k}:")
    print(*sorted(adj_l[S]))
    print()
