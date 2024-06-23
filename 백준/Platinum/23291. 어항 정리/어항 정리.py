import sys


def solve(n, k, fishtank):
    # 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 정리해야하는지
    answer = 0
    while True:
        if max(fishtank[0]) - min(fishtank[0]) <= k:
            break

        # 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
        #    만약, 그러한 어항이 여러개라면 물고기의 수가 최소인 어항 모두에 한 마리씩 넣는다
        min_fishtank_value, min_fishtank_index_list = max(fishtank[0]), []
        for i in range(n):
            fishtank_value = fishtank[0][i]
            if fishtank_value < min_fishtank_value:
                min_fishtank_value = fishtank_value
                min_fishtank_index_list = [i]
            elif fishtank_value == min_fishtank_value:
                min_fishtank_index_list.append(i)
        for i in min_fishtank_index_list:
            fishtank[0][i] += 1

        # 2. 어항을 쌓는다
        #    공중 부양 작업
        v = fishtank[0].pop(0)
        fishtank.insert(0, [v])
        width, height = 1, 2
        while True:
            if (len(fishtank[-1]) - width) < height:
                break
            floating_fishtank = [[0]*height for _ in range(width)]
            for c in range(width):
                for r in range(height):
                    v = fishtank[height-r-1].pop(0)
                    floating_fishtank[c][r] = v
            fishtank.extend(floating_fishtank)
            for i in range(height):
                row = fishtank.pop(0)
                if row:
                    fishtank.append(row)
            width, height = len(fishtank[0]), len(fishtank)

        # 3. 어항에 있는 물고기의 수를 조절
        #    물고기 수의 차이를 5로 나눈 몫: d
        #    d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다
        move_list = []
        for r in range(height):
            current_width = len(fishtank[r])
            for c in range(current_width):
                v = fishtank[r][c]
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < height and 0 <= nc < len(fishtank[nr]):
                        d = (fishtank[r][c] - fishtank[nr][nc])//5
                        if d > 0:
                            move_list.append([r, c, nr, nc, d])
        for sr, sc, er, ec, nv in move_list:
            fishtank[sr][sc] -= nv
            fishtank[er][ec] += nv
        # 4. 다시 어항을 바닥에 일렬로 놓아야 한다
        #    가장 왼쪽에 있는 어항부터, 그리고 아래에 있는 어항부터 가장 위에 있는 어항까지 순서대로 바닥에 놓아야 한다
        new_fishtank = [0]*n
        i = 0
        for c in range(len(fishtank[-1])):
            for r in range(height-1, -1, -1):
                if 0 <= c < len(fishtank[r]):
                    new_fishtank[i] = fishtank[r][c]
                    i += 1
        fishtank = [new_fishtank]

        # 5. 다시 공중 부양 작업
        height = 1
        width = n
        for _ in range(2):
            width //= 2
            floating_fishtank = [[0]*width for _ in range(height)]
            for r in range(height):
                for c in range(width):
                    floating_fishtank[height-r-1][width-c-1] = fishtank[r].pop(0)
            fishtank = floating_fishtank + fishtank
            height *= 2

        # 6. 다시 위에서 한 물고기 조절 작업
        move_list = []
        for r in range(height):
            for c in range(width):
                v = fishtank[r][c]
                for nr, nc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= nr < height and 0 <= nc < width:
                        d = (fishtank[r][c] - fishtank[nr][nc])//5
                        if d > 0:
                            move_list.append([r, c, nr, nc, d])
        for sr, sc, er, ec, nv in move_list:
            fishtank[sr][sc] -= nv
            fishtank[er][ec] += nv

        # 7. 바닥에 일렬로 놓는 작업
        new_fishtank = [0]*n
        i = 0
        for c in range(width):
            for r in range(height-1, -1, -1):
                new_fishtank[i] = fishtank[r][c]
                i += 1
        fishtank = [new_fishtank]
        answer += 1
    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    FISHTANK = list(map(int, input().split()))
    answer = solve(N, K, [FISHTANK])
    print(answer)
