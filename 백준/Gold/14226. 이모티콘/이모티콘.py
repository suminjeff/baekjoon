import sys
input = sys.stdin.readline

from collections import deque


S = int(input())
que = deque([[1, 0]])
visited = {}
visited.setdefault((1, 0), 0)
while que:
    now, clip = que.popleft()
    if now == S:
        print(visited[(now, clip)])
        break

    # 복사하기
    if (now, now) not in visited.keys():
        visited.setdefault((now, now), visited[(now, clip)]+1)
        que.append([now, now])

    # 붙여넣기
    paste = now + clip
    if (paste, clip) not in visited.keys():
        visited.setdefault((paste, clip), visited[(now, clip)]+1)
        que.append([paste, clip])

    # 삭제하기
    delete = now - 1
    if (delete, clip) not in visited.keys():
        visited.setdefault((delete, clip), visited[(now, clip)]+1)
        que.append([delete, clip])

