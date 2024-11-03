from collections import deque

def solution(n):
    dr, dc = [1, 0, -1], [0, 1, -1]
    triangle = [[0]*n for n in range(1, n+1)]
    triangle[0][0] = 1
    cnt = n*(n+1)//2 - 1
    
    que = deque([[0, 0, 0]])
    
    while que and cnt:
        r, c, i = que.popleft()
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < len(triangle[nr]) and triangle[nr][nc] == 0:
            triangle[nr][nc] = triangle[r][c] + 1
            cnt -= 1
            que.append([nr, nc, i])
        else:
            que.append([r, c, (i + 1) % 3])
        
    answer = []
    for r in range(n):
        for v in triangle[r]:
            answer.append(v)
    return answer