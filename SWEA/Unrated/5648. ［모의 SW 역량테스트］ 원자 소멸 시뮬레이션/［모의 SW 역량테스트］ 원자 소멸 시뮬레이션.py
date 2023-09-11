def canContinue():
    global N
    for i in range(4):
        for j in range(len(arr[i])):
            if arr[i][j]:
                return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    max_x = max_y = float("-inf")
    min_x = min_y = float("inf")
    arr = [[] for _ in range(4)]
    # 상(0), 하(1), 좌(2), 우(3)
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
        arr[direction].append([x, y, energy])

    ans = 0
    while canContinue():
        boom = {}
        checker = []
        for i in range(4):
            M = len(arr[i])
            for j in range(M):
                x, y, energy = arr[i].pop(0)

                if i == 0:
                    y += 0.5
                elif i == 1:
                    y -= 0.5
                elif i == 2:
                    x -= 0.5
                elif i == 3:
                    x += 0.5

                if min_x <= x <= max_x and min_y <= y <= max_y:
                    if (x, y) in boom.keys():
                        boom[(x, y)][1] += energy
                        checker.append((x, y))
                    else:
                        boom.setdefault((x, y), [i, energy])
        for key in boom.keys():
            if key in checker:
                ans += boom[key][1]
            else:
                x, y = list(key)
                arr[boom[key][0]].append([x, y, boom[key][1]])

    print(f"#{tc} {ans}")
