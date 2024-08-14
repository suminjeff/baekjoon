from collections import deque, defaultdict


def find_cluster():
    cluster = [[0]*C for _ in range(R)]
    cluster_table = defaultdict(list)
    pk = 1
    for i in range(R):
        for j in range(C):
            if arr[i][j] == space or cluster[i][j] != 0:
                continue
            cluster[i][j] = pk
            cluster_table[pk].append([i, j])
            que = deque([[i, j]])
            while que:
                r, c = que.popleft()
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or arr[nr][nc] == space or cluster[nr][nc] != 0:
                        continue
                    cluster[nr][nc] = pk
                    cluster_table[pk].append([nr, nc])
                    que.append([nr, nc])
            pk += 1
    return cluster, cluster_table


def throw(i, j, d):
    v = direction[d]
    while arr[i][j] == space:
        j += v
        if j < 0 or j >= C:
            return
    arr[i][j] = space


if __name__ == '__main__':
    mineral, space = 'x', '.'
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    N = int(input())
    height = list(map(lambda x: R-x, list(map(int, input().split()))))
    direction = [1, -1]
    for i in range(N):
        # 1. 막대기 던지기
        h = height[i]
        # 왼쪽
        if i % 2 == 0:
            throw(h, 0, 0)
        # 오른쪽
        else:
            throw(h, C-1, 1)
        # 2. 클러스터 업데이트
        cluster, cluster_table = find_cluster()
        # 3. 중력 작용
        gravity_list = []
        for pk in cluster_table.keys():
            min_g = R
            for r, c in cluster_table[pk]:
                g = 0
                same_cluster = False
                for nr in range(r+1, R):
                    if cluster[nr][c] == pk:
                        same_cluster = True
                        break
                    if arr[nr][c] == space:
                        g += 1
                    else:
                        break
                if not same_cluster:
                    min_g = min(min_g, g)
            if min_g == 0:
                continue
            gravity_list.append([pk, min_g])
        # 4. 클러스터 업데이트
        for pk, g in gravity_list:
            for r, c in sorted(cluster_table[pk], key=lambda x: (-x[0])):
                nr = r+g
                arr[r][c], arr[nr][c] = arr[nr][c], arr[r][c]
    [print(''.join(row)) for row in arr]