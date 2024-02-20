import sys
input = sys.stdin.readline
from collections import deque

# 1963

M = 9999
primary = [1]*(M+1)
for i in range(2, M+1):
    if primary[i] == 0:
        continue
    j = 2
    while i*j < M+1:
        primary[i*j] = 0
        j += 1

graph = []
for i in range(1000, M+1):
    if primary[i] == 1:
        graph.append(i)

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    visited = [-1]*(M+1)
    visited[x] = 0
    que = deque([x])
    while que:
        v = que.popleft()
        if v == y:
            break
        # 천의 자리를 바꾸는 경우
        for i in range(4):
            for j in range(10):
                v_string_list = list(str(v))
                if i == 3 and j == 0:
                    continue
                v_string_list[3-i] = str(j)
                nv = int("".join(v_string_list))
                if nv != v and primary[nv] == 1 and visited[nv] == -1:
                    visited[nv] = visited[v]+1
                    que.append(nv)
    print(visited[y])


