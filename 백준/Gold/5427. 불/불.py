import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for tc in range(1, T+1):
    w, h = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(h)]
    me = deque()
    fire = deque()
    visited_fire = [[0]*w for _ in range(h)]
    visited_me = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                visited_me[i][j] = 1
                me.append([i, j, 0])
            elif arr[i][j] == '*':
                visited_fire[i][j] = 1
                fire.append([i, j])
    flag = False
    while me:
        for _ in range(len(fire)):
            fr, fc = fire.popleft()
            for nfr, nfc in [[fr+1, fc], [fr-1, fc], [fr, fc+1], [fr, fc-1]]:
                if 0 <= nfr < h and 0 <= nfc < w and visited_fire[nfr][nfc] == 0 and arr[nfr][nfc] != '#':
                    visited_fire[nfr][nfc], arr[nfr][nfc] = 1, '*'
                    fire.append([nfr, nfc])
        for _ in range(len(me)):
            r, c, t = me.popleft()
            for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < h and 0 <= nc < w and visited_fire[nr][nc] == 0 and visited_me[nr][nc] == 0 and arr[nr][nc] != '#':
                    visited_me[nr][nc] = 1
                    arr[nr][nc] = '@'
                    me.append([nr, nc, t+1])
                elif nr < 0 or nr >= h or nc < 0 or nc >= w:
                    flag = True
        if flag:
            print(t+1)
            break
    if not flag:
        print('IMPOSSIBLE')