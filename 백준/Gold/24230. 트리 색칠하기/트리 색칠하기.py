import sys


def solve(n, c, edges):
    tree = [[] for _ in range(n+1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    answer = 0 if c[0] == 0 else 1

    visited = [0 for _ in range(n+1)]

    stack = [1]
    visited[1] = 1

    while stack:
        v = stack.pop()
        for nv in tree[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                if c[nv-1] != c[v-1]:
                    answer += 1
                stack.append(nv)

    return answer


if __name__ == '__main__':
    N = int(input())
    C = list(map(int, input().split()))
    EDGES = [list(map(int, input().split())) for _ in range(N-1)]
    ANSWER = solve(N, C, EDGES)
    print(ANSWER)