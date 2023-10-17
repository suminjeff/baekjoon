import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    global order
    for w in adj_l[v]:
        if not visited[w]:
            order += 1
            visited[w] = order
            dfs(w)




N, M, R = map(int, input().split())
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
for i in range(1, N+1):
    adj_l[i].sort(reverse=True)
visited = [0]*(N+1)
order = 1
visited[R] = order
dfs(R)
for i in range(1, N+1):
    print(visited[i])