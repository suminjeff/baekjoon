def calc_score(lineup):
    global N
    global max_score
    lineup = lineup[:3] + [0] + lineup[3:]
    score = 0
    i = 0
    for inning in range(N):
        base = [0] * 4
        out = 0
        while out < 3:
            order = lineup[i]
            batter = input_arr[inning][order]
            if batter == 1:
                score += base[3]
                base[1], base[2], base[3] = 1, base[1], base[2]
            elif batter == 2:
                score += base[3] + base[2]
                base[1], base[2], base[3] = 0, 1, base[1]
            elif batter == 3:
                score += base[3] + base[2] + base[1]
                base[1], base[2], base[3] = 0, 0, 1
            elif batter == 4:
                score += base[3] + base[2] + base[1] + 1
                base[1], base[2], base[3] = 0, 0, 0
            elif batter == 0:
                out += 1
            i = (i+1) % 9
    max_score = max(max_score, score)

def perm(arr, n):
    if len(arr) == n:
        # print(arr)
        calc_score(arr)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            arr.append(lineup_idx[i])
            perm(arr, n)
            arr.pop()
            visited[i] = 0




N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
lineup_idx = [1, 2, 3, 4, 5, 6, 7, 8]
visited = [0] * 8
max_score = 0
perm([], 8)
print(max_score)