import sys
from collections import deque


def solve(h, w, building, keys):
    documents = 0

    visited = [[0 for _ in range(w)] for _ in range(h)]

    # 상근이 시작 위치
    visited[0][0] = 1

    # bfs 탐색
    que = deque([(0, 0)])
    while que:
        r, c = que.popleft()
        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < h and 0 <= nc < w and building[nr][nc] != "*" and visited[nr][nc] == 0:
                # 다음 칸이 방문한 적 없는 칸이라면
                nv = building[nr][nc]
                # 다읔 칸이 빈 칸이라면
                if nv == ".":
                    visited[nr][nc] = 1
                    que.append((nr, nc))
                # 다음 칸이 문서라면
                elif nv == "$":
                    building[nr][nc] = "."
                    visited[nr][nc] = 1
                    documents += 1
                    que.append((nr, nc))
                # 다음 칸이 열쇠라면
                elif nv.islower():
                    visited = [[0 for _ in range(w)] for _ in range(h)]
                    visited[nr][nc] = 1
                    building[nr][nc] = "."
                    keys += nv if nv not in keys else ""
                    que.append((nr, nc))
                # 다음 칸이 문이고 키가 있다면
                elif nv.isupper() and nv.lower() in keys:
                    building[nr][nc] = "."
                    visited[nr][nc] = 1
                    que.append((nr, nc))
    return documents

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        H, W = map(int, input().split())
        BUILDING = [["." for _ in range(W+2)]]+[list("."+input()+".") for _ in range(H)]+[["." for _ in range(W+2)]]
        KEYS = input()
        answer = solve(H+2, W+2, BUILDING, KEYS)
        print(answer)
