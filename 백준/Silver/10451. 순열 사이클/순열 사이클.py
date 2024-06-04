import sys
sys.setrecursionlimit(10**6)


def count_sequence_cycles(N, A):
    visited = [False] * (N + 1)

    def dfs(v):
        if visited[v]:
            return

        visited[v] = True
        nv = A[v - 1]
        dfs(nv)

    result = 0
    for v in range(1, N + 1):
        if not visited[v]:
            dfs(v)
            result += 1

    return result


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = count_sequence_cycles(N, A)
    print(ans)
