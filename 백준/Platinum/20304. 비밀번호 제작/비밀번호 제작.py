import sys
from collections import deque


def solve(n, m, passwords):
    distance = [21]*(n+1)
    que = deque()
    for p in passwords:
        distance[p] = 0
        que.append(p)

    answer = 0
    while que:
        v = que.popleft()

        for i in range(20):
            nv = v ^ (1 << i)
            if nv <= n and distance[nv] > distance[v]+1:
                distance[nv] = distance[v]+1
                answer = max(answer, distance[nv])
                que.append(nv)

    return answer


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    PASSWORDS = list(map(int, input().split()))
    ANSWER = solve(N, M, PASSWORDS)
    print(ANSWER)