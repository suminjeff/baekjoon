op = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


T = 1
for tc in range(1, T+1):
    w, h = map(int, input().split())
    N = int(input())
    position = [list(map(int, input().split())) for _ in range(N+1)]
    for i in range(N+1):
        if position[i][0] == 1:
            position[i][1] = [position[i][1], h]
        elif position[i][0] == 2:
            position[i][1] = [position[i][1], 0]
        elif position[i][0] == 3:
            position[i][1] = [0, h - position[i][1]]
        elif position[i][0] == 4:
            position[i][1] = [w, h - position[i][1]]

    dg_pos, dg_coor = position[-1]

    ans = 0
    for i in range(N):
        store_pos, store_coor = position[i]
        if op[dg_pos] == store_pos:
            if dg_pos == 1 or dg_pos == 2:
                left = (dg_coor[0]) + (store_coor[0])
                right = (w - dg_coor[0]) + (w - store_coor[0])
                ans += h + min(left, right)
            elif dg_pos == 3 or dg_pos == 4:
                up = (h - dg_coor[1]) + (h - store_coor[1])
                down = (dg_coor[1]) + (store_coor[1])
                ans += w + min(up, down)
        else:
            ans += abs(dg_coor[0]-store_coor[0]) + abs(dg_coor[1]-store_coor[1])
    print(ans)