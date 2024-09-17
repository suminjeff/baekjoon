import sys
from heapq import heappop, heappush


def dijkstra(start, h, w, prison):
    sr, sc = start
    keys = [[sys.maxsize]*w for _ in range(h)]
    keys[sr][sc] = 0

    heap = [[0, sr, sc]]
    while heap:
        k, r, c = heappop(heap)

        if keys[r][c] < k:
            continue

        for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
            if 0 <= nr < h and 0 <= nc < w and prison[nr][nc] != '*':
                nk = keys[r][c] + int(prison[nr][nc] == '#')
                if keys[nr][nc] > nk:
                    keys[nr][nc] = nk
                    heappush(heap, [nk, nr, nc])

    return keys


def solve(h, w, prison):
    prisoner = []
    for r in range(h):
        for c in range(w):
            if prison[r][c] == '$':
                prisoner.append([r, c])

    p1, p2 = prisoner
    d1, d2, d3 = dijkstra(p1, h, w, prison), dijkstra(p2, h, w, prison), dijkstra([0, 0], h, w, prison)

    answer = sys.maxsize
    for r in range(h):
        for c in range(w):
            if d1[r][c] != sys.maxsize and d2[r][c] != sys.maxsize and d3[r][c] != sys.maxsize:
                result = d1[r][c] + d2[r][c] + d3[r][c]
                if prison[r][c] == '*':
                    continue
                if prison[r][c] == '#':
                    result -= 2
                answer = min(answer, result)

    return answer


if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        H, W = map(int, input().split())
        PRISON = ['.'*(W+2)] + ['.'+input()+'.' for _ in range(H)] + ['.'*(W+2)]
        ANSWER = solve(H+2, W+2, PRISON)
        print(ANSWER)