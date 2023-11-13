import sys

input = sys.stdin.readline
from collections import deque


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    dp = [0] * (N + 1)

    adj_l = [[] for _ in range(N + 1)]
    counts = [-1] + [0]*N
    for _ in range(K):
        s, e = map(int, input().split())
        adj_l[s].append(e)
        counts[e] += 1
    W = int(input())

    que = deque()
    for i in range(1, N+1):
        if counts[i] == 0:
            que.append(i)
            dp[i] = time[i]

    while que:
        now = que.popleft()
        for next_node in adj_l[now]:
            counts[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[now]+time[next_node])
            if counts[next_node] == 0:
                que.append(next_node)
        if counts[W] == 0:
            print(dp[W])
            break
