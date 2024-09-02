import sys
sys.setrecursionlimit(10**5)


def solve(v, e, edges):
    parents = [x for x in range(v+1)]

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        p, q = find(x), find(y)
        parents[max(p, q)] = min(p, q)

    edges.sort(key=lambda x: x[2])
    answer = 0
    for x, y, c in edges:
        if find(x) != find(y):
            union(x, y)
            answer += c

    return answer


if __name__ == '__main__':
    V, E = map(int, input().split())
    EDGES = [list(map(int, input().split())) for _ in range(E)]
    ANSWER = solve(V, E, EDGES)
    print(ANSWER)