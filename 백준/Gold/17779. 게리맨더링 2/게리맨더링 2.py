import sys
input = sys.stdin.readline


# 꼭지점 정하기
def point(n):
    global min_v
    for x in range(n-2):
        for y in range(1, n-1):
            for d1 in range(1, n-1):
                for d2 in range(1, n-1):
                    if (0 <= x+d1 < N and 0 <= y-d1 < N) and (0 <= x+d2 < N and 0 <= y+d2 < N) and (0 <= x+d1+d2 < N and 0 <= y-d1+d2) and (0 <= x+d2+d1 < N and 0 <= y+d2-d1 < N):
                        v = divide(x, y, d1, d2)
                        min_v = min(min_v, v)


def divide(x, y, d1, d2):
    section = [0]*5
    visited = [[0]*N for _ in range(N)]
    delta = [[1, -1], [1, 1]]
    cx, cy = x+1, y
    centers = []
    for i in range(d1):
        centers.append([cx, cy])
        nx, ny = cx + delta[1][0], cy + delta[1][1]
        for j in range(d2-1):
            centers.append([nx, ny])
            nx += delta[1][0]
            ny += delta[1][1]
        cx += delta[0][0]
        cy += delta[0][1]

    # section 5
    for cx, cy in centers:
        visited[cx][cy] = 1
        section[4] += arr[cx][cy]
        delta = [[cx+1, cy], [cx, cy+1], [cx-1, cy], [cx, cy-1]]
        for nx, ny in delta:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                section[4] += arr[nx][ny]

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                if 0 <= r < x+d1 and 0 <= c <= y:
                    section[0] += arr[r][c]
                elif 0 <= r <= x+d2 and y < c < N:
                    section[1] += arr[r][c]
                elif x+d1 <= r < N and 0 <= c < y-d1+d2:
                    section[2] += arr[r][c]
                elif x+d2 < r < N and y-d1+d2 <= c < N:
                    section[3] += arr[r][c]
                else:
                    section[4] += arr[r][c]
    return max(section) - min(section)


delta5 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')
point(N)
print(min_v)