def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    que = [[0, 0]]
    while que:
        r, c = que.pop(0)
        v = maps[r][c]
        maps[r][c] = 0
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1:
                maps[nr][nc] = v + 1
                if nr == n-1 and nc == m-1:
                    answer = maps[nr][nc]
                    return answer
                que.append([nr, nc])
    return answer
