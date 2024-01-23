def solution(board):
    N, M = len(board), len(board[0])
    start, goal = [], []
    visited = [[-1]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                visited[i][j] = 0
                start = [i, j]
            elif board[i][j] == "G":
                goal = [i, j]
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    que = [start]
    answer = -1
    while que:
        r, c = que.pop(0)
        if [r, c] == goal:
            answer = visited[r][c]
            break
        for i in range(4):
            dr, dc = delta[i]
            nr, nc = r, c
            while True:
                mr, mc = nr+dr, nc+dc
                if 0 <= mr < N and 0 <= mc < M and board[mr][mc] != "D":
                    nr, nc = mr, mc
                else:
                    break
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c]+1
                que.append([nr, nc])
                
    return answer