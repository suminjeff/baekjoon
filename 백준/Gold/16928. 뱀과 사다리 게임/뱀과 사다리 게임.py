import sys
input = sys.stdin.readline

from collections import deque


board = [0]*101
visited = [0]*101
ladder = {}
snake = {}
N, M = map(int, input().split())
for _ in range(N):
    s, e = map(int, input().split())
    ladder.setdefault(s, e)
for _ in range(M):
    s, e = map(int, input().split())
    snake.setdefault(s, e)

que = deque()
start = 1
que.append(start)
while que:
    v = que.popleft()
    if v == 100:
        print(board[v])
        continue
    for dice in range(1, 7):
        w = v + dice
        if w <= 100 and not visited[w]:
            if w in ladder.keys():
                w = ladder[w]
            elif w in snake.keys():
                w = snake[w]
            if not visited[w]:
                visited[w] = True
                board[w] = board[v]+1
                que.append(w)
